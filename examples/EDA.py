import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Configure visual aesthetics
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'figure.autolayout': True})

# Configuration & Embedded SQL for Data Extraction
# -----------------------------------------------------------------------------
# OPTIMIZED SQL EXTRACTION QUERY (For backend engineering team)
# SELECT
#     e.EmployeeNumber, e.Age, e.Gender, e.MaritalStatus, e.DistanceFromHome,
#     c.MonthlyIncome, c.PercentSalaryHike, c.StockOptionLevel,
#     t.TotalWorkingYears, t.YearsAtCompany, t.YearsInCurrentRole,
#     t.YearsSinceLastPromotion, t.YearsWithCurrManager, t.NumCompaniesWorked,
#     j.Department, j.JobRole, j.JobLevel, j.BusinessTravel, j.OverTime,
#     s.JobSatisfaction, s.EnvironmentSatisfaction, s.RelationshipSatisfaction,
#     s.WorkLifeBalance, s.PerformanceRating, s.TrainingTimesLastYear,
#     e.Attrition
# FROM Employees e
# JOIN Compensation c ON e.EmployeeID = c.EmployeeID
# JOIN Tenure t ON e.EmployeeID = t.EmployeeID
# JOIN JobDetails j ON e.EmployeeID = j.EmployeeID
# JOIN Surveys s ON e.EmployeeID = s.EmployeeID;
# -----------------------------------------------------------------------------

FILE_PATH = 'IBM Attrition.csv'
PLOT_DIR = 'EDA_Plots'
TEXT_OUTPUT = 'EDA_Statistical_Analysis.txt'

# Create output directory for graphs
if not os.path.exists(PLOT_DIR):
    os.makedirs(PLOT_DIR)

# Variable definitions (Including NumCompaniesWorked & TrainingTimesLastYear)
CONTINUOUS_VARS = [
    'Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 'MonthlyIncome',
    'MonthlyRate', 'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears',
    'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager'
]

CATEGORICAL_VARS = [
    'BusinessTravel', 'Department', 'EducationField', 'Gender',
    'JobRole', 'MaritalStatus', 'OverTime'
]

ORDINAL_VARS = [
    'Education', 'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel',
    'JobSatisfaction', 'PerformanceRating', 'RelationshipSatisfaction',
    'StockOptionLevel', 'TrainingTimesLastYear', 'WorkLifeBalance'
]


def plot_attrition_bars(df, col, ax, title, is_continuous=False, is_ordinal=False):
    """
    Plots a grouped side-by-side bar chart (Retained vs Attrition) and annotates it with N, Attr_Pct, and Ret_Pct.
    If continuous, it bins the data first.
    """
    plot_df = df.copy()

    # Bin continuous variables for the bar chart view
    if is_continuous:
        plot_df[f'{col}_Binned'] = pd.qcut(
            plot_df[col], q=5, duplicates='drop')
        target_col = f'{col}_Binned'
    else:
        target_col = col

    # Calculate Cross-tabulation
    ct = pd.crosstab(plot_df[target_col], plot_df['Attrition'])

    # Ensure columns exist even if no 'Yes' or 'No' values
    if 'Yes' not in ct:
        ct['Yes'] = 0
    if 'No' not in ct:
        ct['No'] = 0

    ct['Total'] = ct['Yes'] + ct['No']
    ct['Attr_Pct'] = (ct['Yes'] / ct['Total']) * 100
    ct['Ret_Pct'] = (ct['No'] / ct['Total']) * 100

    # Sort Categorical variables in DESC order. (Preserve sequential for ordinal/continuous)
    if not is_continuous and not is_ordinal:
        ct = ct.sort_values(by='Total', ascending=False)

    # Plot Side-by-Side Bars
    x_labels = [str(idx) for idx in ct.index]
    x = np.arange(len(x_labels))
    width = 0.40

    bars_no = ax.bar(x - width/2, ct['No'],
                     width, color='#2ecc71', label='Retained')
    bars_yes = ax.bar(x + width/2, ct['Yes'],
                      width, color='#e74c3c', label='Attrition')

    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_ylabel('Employee Count')
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels)

    if len(x_labels) > 4 or is_continuous:
        ax.tick_params(axis='x', rotation=45)
    ax.legend(loc='upper right')

    max_y = max(ct['No'].max(), ct['Yes'].max())
    ax.set_ylim(0, max_y * 1.25)

    # Annotate bars
    for i, idx in enumerate(ct.index):
        total = ct.loc[idx, 'Total']
        yes = ct.loc[idx, 'Yes']
        no = ct.loc[idx, 'No']
        attr_pct = ct.loc[idx, 'Attr_Pct']
        ret_pct = ct.loc[idx, 'Ret_Pct']

        if total == 0:
            continue

        ax.text(x[i] - width/2, no + (max_y * 0.015),
                f"Ret: {ret_pct:.1f}%", ha='center', va='bottom', color='#27ae60', fontweight='bold', fontsize=8)
        ax.text(x[i] + width/2, yes + (max_y * 0.015),
                f"Attr: {attr_pct:.1f}%", ha='center', va='bottom', color='#c0392b', fontweight='bold', fontsize=8)

        local_max = max(no, yes)
        ax.text(x[i], local_max + (max_y * 0.08),
                f"N={total}", ha='center', va='bottom', fontweight='bold', color='black', fontsize=10)


def calculate_variable_impact(df, cols, is_continuous=False):
    """
    Calculates the 'Effect Size' of a variable by finding the maximum spread in 
    attrition rates across its categories/bins. Includes a noise filter for low N.
    """
    impacts = []
    # Statistical noise filter: Ignore categories with less than 15 people
    min_n_threshold = 15

    for col in cols:
        if col not in df.columns:
            continue
        plot_df = df.copy()

        if is_continuous:
            plot_df[f'{col}_Binned'] = pd.qcut(
                plot_df[col], q=5, duplicates='drop')
            target = f'{col}_Binned'
        else:
            target = col

        # Calculate rates
        ct = pd.crosstab(plot_df[target], plot_df['Attrition'])
        if 'Yes' not in ct:
            ct['Yes'] = 0
        if 'No' not in ct:
            ct['No'] = 0

        ct['Total'] = ct['Yes'] + ct['No']
        ct['Attr_Pct'] = (ct['Yes'] / ct['Total']) * 100

        # Filter out low-N noise
        valid_ct = ct[ct['Total'] >= min_n_threshold]

        if len(valid_ct) > 1:  # Need at least 2 valid categories to find a spread
            max_rate_idx = valid_ct['Attr_Pct'].idxmax()
            min_rate_idx = valid_ct['Attr_Pct'].idxmin()

            max_rate = valid_ct.loc[max_rate_idx, 'Attr_Pct']
            min_rate = valid_ct.loc[min_rate_idx, 'Attr_Pct']

            spread = max_rate - min_rate
            highest_risk_count = valid_ct.loc[max_rate_idx, 'Total']
            highest_risk_attr_count = valid_ct.loc[max_rate_idx, 'Yes']

            impacts.append({
                'Variable': col,
                'Impact_Spread_Pct': spread,
                'Highest_Risk_Cohort': str(max_rate_idx),
                'Cohort_Attr_Rate': max_rate,
                'Cohort_Total_N': highest_risk_count,
                'Cohort_Attr_N': highest_risk_attr_count
            })

    return impacts


def main():
    f = open(TEXT_OUTPUT, 'w', encoding='utf-8')

    def out(text=""):
        print(text)
        f.write(text + "\n")

    out("="*85)
    out("🚀 INITIATING FULL EDA ENGINE: HR ATTRITION ANALYSIS")
    out("="*85)

    try:
        df = pd.read_csv(FILE_PATH)
        out(
            f"[*] Successfully loaded dataset: {df.shape[0]} rows, {df.shape[1]} columns.\n")
    except FileNotFoundError:
        out(f"[!] Error: Could not find '{FILE_PATH}'. Please ensure it is in the same directory.")
        f.close()
        return

    if 'Attrition' not in df.columns:
        out("[!] Target variable 'Attrition' not found. Exiting.")
        f.close()
        return

    # =========================================================================
    # PHASE 0: EXECUTIVE SUMMARY - HIGHEST IMPACT VARIABLES
    # =========================================================================
    out("--- 0. EXECUTIVE SUMMARY: KEY DRIVERS OF ATTRITION ---")
    out("Ranking variables by 'Effect Spread' (The percentage difference in attrition")
    out("between the highest-risk group and lowest-risk group within that variable).")
    out("Statistical Note: Cohorts with N < 15 are excluded to prevent small-sample noise.\n")

    all_impacts = []
    all_impacts.extend(calculate_variable_impact(
        df, CONTINUOUS_VARS, is_continuous=True))
    all_impacts.extend(calculate_variable_impact(
        df, CATEGORICAL_VARS, is_continuous=False))
    all_impacts.extend(calculate_variable_impact(
        df, ORDINAL_VARS, is_continuous=False))

    # Sort by highest impact descending
    all_impacts_sorted = sorted(
        all_impacts, key=lambda x: x['Impact_Spread_Pct'], reverse=True)

    out(f"{'Rank':<5} | {'Variable Name':<25} | {'Effect Spread':<15} | {'Highest Risk Cohort Details'}")
    out("-" * 100)

    for i, item in enumerate(all_impacts_sorted[:15]):  # Top 15 drivers
        rank = i + 1
        var_name = item['Variable']
        spread = f"{item['Impact_Spread_Pct']:.1f}%"
        risk_cohort = item['Highest_Risk_Cohort']
        risk_rate = f"{item['Cohort_Attr_Rate']:.1f}%"
        risk_n = item['Cohort_Total_N']
        risk_attr = item['Cohort_Attr_N']

        cohort_details = f"'{risk_cohort}' -> {risk_rate} Attrition (Lost {risk_attr} of {risk_n} total)"
        out(f"{rank:<5} | {var_name:<25} | {spread:<15} | {cohort_details}")
    out("\n")

    # =========================================================================
    # PHASE 1: Target Variable Distribution
    # =========================================================================
    out("--- 1. TARGET VARIABLE: BASELINE ATTRITION ---")
    attrition_counts = df['Attrition'].value_counts()
    attrition_pct = df['Attrition'].value_counts(normalize=True) * 100

    out(f"Total Employees: {len(df)}")
    out(f"Retained: {attrition_counts.get('No', 0)} ({attrition_pct.get('No', 0):.2f}%)")
    out(f"Attrition: {attrition_counts.get('Yes', 0)} ({attrition_pct.get('Yes', 0):.2f}%)")
    out(f"-> BASELINE ATTRITION RATE: {attrition_pct.get('Yes', 0):.2f}%\n")

    # =========================================================================
    # PHASE 2: Univariate Analysis (Individual Variables)
    # =========================================================================
    out("--- 2. UNIVARIATE ANALYSIS (INDIVIDUAL VARIABLES) ---")

    out("\n--- 2.1 CONTINUOUS VARIABLES ---")
    for var in CONTINUOUS_VARS:
        if var in df.columns:
            out(f"\n{var.upper()}:")
            var_mean = df[var].mean()
            var_median = df[var].median()
            var_std = df[var].std()
            var_iqr = df[var].quantile(0.75) - df[var].quantile(0.25)

            # Statistical Output
            out(f"  Summary -> Mean: {var_mean:.2f} | Median: {var_median:.2f} | StdDev: {var_std:.2f} | IQR: {var_iqr:.2f}")

            # Visualization: Histogram + Boxplot
            fig, axes = plt.subplots(1, 2, figsize=(14, 5))

            sns.histplot(data=df, x=var, kde=True, ax=axes[0], color='#3498db')
            axes[0].set_title(
                f'{var} - Distribution (Histogram)', fontweight='bold')
            axes[0].set_ylabel('Frequency')

            sns.boxplot(x=df[var], ax=axes[1], color='#3498db')
            axes[1].set_title(
                f'{var} - Spread & Outliers (Box Plot)', fontweight='bold')

            plt.savefig(os.path.join(
                PLOT_DIR, f'01_Univariate_Continuous_{var}.png'), bbox_inches='tight')
            plt.close()

    out("\n--- 2.2 CATEGORICAL VARIABLES ---")
    for var in CATEGORICAL_VARS:
        if var in df.columns:
            out(f"\n{var.upper()}:")
            val_counts = df[var].value_counts()
            val_pcts = df[var].value_counts(normalize=True) * 100

            out(f"  {'Category':<25} | {'Count':<8} | {'Percentage'}")
            out("  " + "-"*55)
            for cat in val_counts.index:
                out(
                    f"  {str(cat):<25} | {val_counts[cat]:<8} | {val_pcts[cat]:.2f}%")

            # Visualization: Annotated Bar Chart
            fig, ax = plt.subplots(figsize=(10, 5))
            sns.countplot(data=df, x=var, order=val_counts.index,
                          ax=ax, palette='viridis', hue=df[var], legend=False)
            ax.set_title(f'{var} - Frequency Bar Chart', fontweight='bold')
            ax.set_ylabel('Count')

            if len(val_counts) > 4:
                ax.tick_params(axis='x', rotation=45)

            # Annotate bars with count and percentage
            for i, p in enumerate(ax.patches):
                cat_name = val_counts.index[i]
                pct = val_pcts[cat_name]
                ax.annotate(f'{int(p.get_height())}\n({pct:.1f}%)',
                            (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='bottom', fontsize=9, fontweight='bold')

            # Add headroom for annotations
            ax.set_ylim(0, val_counts.max() * 1.15)

            plt.savefig(os.path.join(
                PLOT_DIR, f'01_Univariate_Categorical_{var}.png'), bbox_inches='tight')
            plt.close()

    out("\n--- 2.3 ORDINAL VARIABLES ---")
    for var in ORDINAL_VARS:
        if var in df.columns:
            out(f"\n{var.upper()}:")

            # Sort by Index to maintain logical sequence
            val_counts = df[var].value_counts().sort_index()
            total = val_counts.sum()
            cum_pct = (val_counts.cumsum() / total) * 100

            try:
                var_median = df[var].median()
            except:
                var_median = "N/A"
            var_mode = df[var].mode()[0]

            out(
                f"  Summary -> Median Rank: {var_median} | Mode (Most Frequent): {var_mode}")
            out(f"  {'Rank/Value':<12} | {'Count':<8} | {'Cumulative %'}")
            out("  " + "-"*40)
            for cat in val_counts.index:
                out(
                    f"  {str(cat):<12} | {val_counts[cat]:<8} | {cum_pct[cat]:.2f}%")

            # Visualization: Pareto Chart (Ordered Bar + Cumulative %)
            fig, ax1 = plt.subplots(figsize=(10, 5))
            x_labels = [str(x) for x in val_counts.index]
            x_pos = np.arange(len(x_labels))

            # Bar Chart (Counts)
            bars = ax1.bar(x_pos, val_counts.values, color='#9b59b6')
            ax1.set_xticks(x_pos)
            ax1.set_xticklabels(x_labels)
            ax1.set_ylabel('Count', color='#9b59b6', fontweight='bold')
            ax1.set_title(
                f'{var} - Ordered Bar & Cumulative % (Pareto)', fontweight='bold')

            # Cumulative Percentage Line
            ax2 = ax1.twinx()
            ax2.plot(x_pos, cum_pct.values, color='#e74c3c',
                     marker='o', linewidth=2)
            ax2.set_ylabel('Cumulative Percentage (%)',
                           color='#e74c3c', fontweight='bold')
            ax2.set_ylim(0, 110)

            # Annotate line with cum %
            for i, txt in enumerate(cum_pct.values):
                ax2.annotate(f"{txt:.1f}%", (x_pos[i], cum_pct.values[i] + 3),
                             ha='center', fontsize=8, fontweight='bold', color='#c0392b')

            plt.savefig(os.path.join(
                PLOT_DIR, f'01_Univariate_Ordinal_{var}.png'), bbox_inches='tight')
            plt.close()

    # =========================================================================
    # PHASE 3: Continuous Variables vs Attrition
    # =========================================================================
    out("\n--- 3. CONTINUOUS VARIABLES vs ATTRITION ---")
    for var in CONTINUOUS_VARS:
        if var in df.columns:
            out(f"\n{var.upper()}:")

            out("  --- Comprehensive Statistics ---")
            out(f"  {'Group':<12} | {'Mean':<8} | {'StdDev':<8} | {'Min_Value':<9} | {'Q1_25th':<8} | {'Median':<8} | {'Q3_75th':<8} | {'Max_Value':<9} | {'IQR':<8}")

            # Calculate Overall Statistics
            desc_all = df[var].describe()
            iqr_all = desc_all['75%'] - desc_all['25%']
            out(f"  {'Overall':<12} | {desc_all['mean']:<8.2f} | {desc_all['std']:<8.2f} | {desc_all['min']:<9.2f} | {desc_all['25%']:<8.2f} | {desc_all['50%']:<8.2f} | {desc_all['75%']:<8.2f} | {desc_all['max']:<9.2f} | {iqr_all:<8.2f}")

            # Calculate Grouped Statistics (Retained vs Attrition)
            desc_grp = df.groupby('Attrition')[var].describe()
            for grp in ['No', 'Yes']:
                if grp in desc_grp.index:
                    label = 'Retained' if grp == 'No' else 'Attrition'
                    r = desc_grp.loc[grp]
                    iqr_grp = r['75%'] - r['25%']
                    out(f"  {label:<12} | {r['mean']:<8.2f} | {r['std']:<8.2f} | {r['min']:<9.2f} | {r['25%']:<8.2f} | {r['50%']:<8.2f} | {r['75%']:<8.2f} | {r['max']:<9.2f} | {iqr_grp:<8.2f}")

            Q1 = desc_all['25%']
            Q3 = desc_all['75%']
            IQR = iqr_all
            lower_limit = Q1 - (1.5 * IQR)
            upper_limit = Q3 + (1.5 * IQR)

            outliers = df[(df[var] < lower_limit) |
                          (df[var] > upper_limit)][var]

            if not outliers.empty:
                out(
                    f"\n  [!] Statistical Outliers Detected: Found {len(outliers)}")
                out(
                    f"      Limits applied -> Lower Limit: {lower_limit:.2f} | Upper Limit: {upper_limit:.2f}")
            else:
                out(f"\n  [+] No statistical outliers exist.")

            fig, axes = plt.subplots(1, 2, figsize=(16, 6))

            sns.boxplot(x='Attrition', y=var, data=df, ax=axes[0], order=[
                        'Yes', 'No'], palette={'Yes': '#e74c3c', 'No': '#2ecc71'})
            axes[0].set_title(
                f'{var} Outliers & Spread by Attrition', fontweight='bold')

            for i, cat in enumerate(['Yes', 'No']):
                s = df[df['Attrition'] == cat][var].dropna()
                q1 = s.quantile(0.25)
                q3 = s.quantile(0.75)
                iqr = q3 - q1
                lower = q1 - 1.5 * iqr
                upper = q3 + 1.5 * iqr

                cat_outliers = s[(s < lower) | (s > upper)]
                for val in cat_outliers.unique():
                    axes[0].text(i + 0.05, val, f"{val:g}", va='center',
                                 ha='left', fontsize=9, fontweight='bold', color='#34495e')

            plot_attrition_bars(
                df, var, axes[1], f'{var} (Binned) Attrition Rates', is_continuous=True)

            plt.suptitle(
                f'Bivariate EDA: {var} vs Attrition', fontsize=16, fontweight='bold')
            plt.savefig(os.path.join(
                PLOT_DIR, f'02_Continuous_{var}.png'), bbox_inches='tight')
            plt.close()

    # =========================================================================
    # PHASE 4: Categorical & Ordinal Variables vs Attrition
    # =========================================================================
    COMBINED_CATS = CATEGORICAL_VARS + ORDINAL_VARS
    out("\n--- 4. CATEGORICAL & ORDINAL VARIABLES vs ATTRITION ---")

    for var in COMBINED_CATS:
        if var in df.columns:
            out(f"\n{var.upper()}:")

            ct = pd.crosstab(df[var], df['Attrition'])
            if 'Yes' not in ct:
                ct['Yes'] = 0
            if 'No' not in ct:
                ct['No'] = 0
            ct['Total'] = ct['Yes'] + ct['No']
            ct['Attr_Rate'] = (ct['Yes'] / ct['Total']) * 100

            if var in ORDINAL_VARS:
                ct = ct.sort_index()
            else:
                ct = ct.sort_values('Total', ascending=False)

            for idx, row in ct.iterrows():
                flag = "[!] High Risk" if row['Attr_Rate'] > (
                    attrition_pct.get('Yes', 0) * 1.5) else ""
                out(f"  {idx}: N={row['Total']} | Attrition: {row['Yes']} | Attrition Rate: {row['Attr_Rate']:.2f}% {flag}")

            fig, ax = plt.subplots(figsize=(10, 6))
            is_ord = var in ORDINAL_VARS
            plot_attrition_bars(
                df, var, ax, f'{var} Attrition Rates', is_continuous=False, is_ordinal=is_ord)

            plt.savefig(os.path.join(
                PLOT_DIR, f'03_Categorical_Ordinal_{var}.png'), bbox_inches='tight')
            plt.close()

    # =========================================================================
    # PHASE 5: Outliers & Quality Checks
    # =========================================================================
    out("\n" + "="*85)
    out("🛠️ PHASE 5: DATA QUALITY & OUTLIERS")
    out("="*85)

    # 5.1 Tenure Logical Violations
    out("--- 5.1 Tenure Logic Checks ---")
    if all(c in df.columns for c in ['YearsAtCompany', 'TotalWorkingYears', 'Age']):
        v1 = df[df['YearsAtCompany'] > df['TotalWorkingYears']]
        out(f"  [!] Rows where YearsAtCompany > TotalWorkingYears: {len(v1)}")
        if not v1.empty:
            out("      Exact Violation Values (YearsAtCompany, TotalWorkingYears):")
            for idx, r in v1.iterrows():
                out(
                    f"      - Row {idx}: YAC={r['YearsAtCompany']} | TWY={r['TotalWorkingYears']}")

        df['Start_Age'] = df['Age'] - df['TotalWorkingYears']
        v2 = df[df['Start_Age'] < 18]
        out(f"  [!] Rows where estimated starting age < 18: {len(v2)}")
        if not v2.empty:
            out(
                f"      Min estimated start age found: {v2['Start_Age'].min()}")

    # 5.2 Compensation Outliers
    out("\n--- 5.2 Compensation Outliers (By Job Level) ---")
    if all(c in df.columns for c in ['MonthlyIncome', 'JobLevel']):
        percentiles_99 = df.groupby('JobLevel')['MonthlyIncome'].quantile(0.99)
        outliers_found = False
        for level, threshold in percentiles_99.items():
            level_outliers = df[(df['JobLevel'] == level)
                                & (df['MonthlyIncome'] > threshold)]
            if not level_outliers.empty:
                outliers_found = True
                out(f"  Job Level {level}: 99th Pct Threshold = ${threshold:.2f} | Found {len(level_outliers)} outliers.")
        if not outliers_found:
            out("  No extreme compensation outliers found past the 99th percentile.")

    # 5.3 Redundancy
    out("\n--- 5.3 Redundancy & Variance Checks ---")
    rate_cols = ['DailyRate', 'HourlyRate', 'MonthlyRate', 'MonthlyIncome']
    available_rates = [c for c in rate_cols if c in df.columns]

    if len(available_rates) > 1:
        corr_matrix = df[available_rates].corr()
        upper_tri = corr_matrix.where(
            np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        highly_correlated = [
            column for column in upper_tri.columns if any(upper_tri[column] > 0.95)]
        if highly_correlated:
            out(
                f"  [!] Warning: Highly redundant financial columns found: {highly_correlated}")
        else:
            out("  [+] Financial rate variables appear independent.")

    # Variance Check
    variance_flag = False
    for col in df.columns:
        unique_counts = df[col].nunique()
        if unique_counts == 1:
            out(f"  [!] ZERO VARIANCE: '{col}' has only 1 unique value.")
            variance_flag = True
    if not variance_flag:
        out("\n  [+] No zero-variance columns detected.")

    out("\n" + "="*85)
    out(f"✅ EDA EXECUTION COMPLETE!")
    out(f"📂 Visualizations saved securely in the './{PLOT_DIR}' directory.")
    out(f"📄 Statistical Analysis saved to './{TEXT_OUTPUT}'")
    out("="*85)

    f.close()


if __name__ == "__main__":
    main()
