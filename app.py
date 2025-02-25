import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Lok-Sabha-Election-2024-Analysis", layout="centered")


# Title
st.title("📊 Election Data Dashboard")

st.markdown("""
    ### Welcome to the Election Dashboard
    ###### This dashboard allows you to explore various aspects of the Lok Sabha elections, including party performance, winning margins, and more.
    ###### Use the filters in the sidebar to customize the data you want to analyze.
    
""")


# Load Data Directly from Files
file1 = "Dataset/candidates_with_phase.csv"
file2 = "Dataset/results_2024.csv"
file3 = "Dataset/results_2024_winners.csv"

df_candidates = pd.read_csv(file1)
df_results = pd.read_csv(file2)
df_winners = pd.read_csv(file3)

# Merge winners with candidates data to get age
df_winners = df_winners.merge(df_candidates[['State', 'Constituency_No', 'Constituency', 'Candidate Name', 'Age', 'Gender']],
                              left_on=['State', 'PC No', 'PC Name', 'Winning Candidate'],
                              right_on=['State', 'Constituency_No', 'Constituency', 'Candidate Name'],
                              how="left",suffixes=('', '_candidate'))

# Drop unnecessary columns
df_winners.drop(columns=['Constituency_No', 'Constituency', 'Candidate Name'], inplace=True)

# Sidebar - Select Visualization
st.sidebar.header("📌 Explore Voting Trends")
visualization = st.sidebar.radio("Select a Trent to Visualize", [
    "Gender Distribution", "Age Distribution",
    "Phase-wise Candidate Distribution", "State-wise Candidate Count",
    "Seats Won by Each Party", "Party-wise Victory Rate",
    "Candidate Success by Age", "Gender-wise Winning Trends",'Regional result',"Candidates Contested vs. Seats Won",
    "Top 10 Closest Contests","Top 10 Largest Winning Margins"
])




# Visualizations
# Dynamic Filters Based on Selection
if visualization == "Gender Distribution":
    st.sidebar.header("🔍 Filters for Gender Distribution")
    gender_options = df_candidates["Gender"].unique()
    gender_filter = st.sidebar.multiselect("Select Gender", ["Select All"] + list(gender_options), default=gender_options)

    if "Select All" in gender_filter:
        gender_filter = gender_options

    filtered_df = df_candidates[df_candidates["Gender"].isin(gender_filter)]
    st.write(f"### Selected Data Count: {len(filtered_df)} Candidates")

    # --- Gender Distribution ---
    st.subheader("📊 Gender Distribution of Candidates")
    fig, ax = plt.subplots(figsize=(7, 5), facecolor='darkgrey')
    ax.set_facecolor('rosybrown')
    sns.countplot(data=filtered_df, x="Gender", hue='Gender', palette='viridis', ax=ax, edgecolor="black", linewidth=1.5)
    plt.title("Gender Distribution", fontsize=14, fontweight='bold', color="darkblue")
    plt.xlabel("Gender", fontsize=12, fontweight='bold', color="darkgreen")
    plt.ylabel("Count", fontsize=12, fontweight='bold', color="darkred")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

elif visualization == "Age Distribution":
    st.sidebar.header("🔍 Filters for Age Distribution")
    age_range = st.sidebar.slider("Select Age Range", int(df_candidates["Age"].min()), int(df_candidates["Age"].max()), (int(df_candidates["Age"].min()), int(df_candidates["Age"].max())))

    filtered_df = df_candidates[df_candidates["Age"].between(age_range[0], age_range[1])]
    st.write(f"### Selected Data Count: {len(filtered_df)} Candidates")

    # --- Age Distribution ---
    st.subheader("📊 Age Distribution of Candidates")
    fig, ax = plt.subplots(figsize=(9, 5), facecolor='plum')
    ax.set_facecolor('orange')
    sns.histplot(filtered_df["Age"], bins=15, kde=True, color="#1f77b4", alpha=0.8, edgecolor="black", linewidth=1.2, ax=ax)
    sns.kdeplot(filtered_df["Age"], color="purple", linewidth=2, linestyle="--", ax=ax)
    plt.title("Age Distribution", fontsize=14, fontweight='bold', color="darkblue")
    plt.xlabel("Age", fontsize=12, fontweight='bold', color="darkgreen")
    plt.ylabel("Count", fontsize=12, fontweight='bold', color="darkred")
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    st.pyplot(fig)

elif visualization == "Phase-wise Candidate Distribution":
    st.sidebar.header("🔍 Filters for Phase-wise Distribution")
    phase_options = df_candidates["Phase"].unique()
    phase_filter = st.sidebar.multiselect("Select Election Phase", ["Select All"] + list(phase_options), default=phase_options)

    if "Select All" in phase_filter:
        phase_filter = phase_options

    filtered_df = df_candidates[df_candidates["Phase"].isin(phase_filter)]
    st.write(f"### Selected Data Count: {len(filtered_df)} Candidates")

    # --- Phase-wise Candidate Distribution ---
    st.subheader("📊 Phase-wise Candidate Distribution")
    phase_counts = filtered_df['Phase'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='teal')
    sns.barplot(x=phase_counts.index, y=phase_counts.values, hue=phase_counts.index, palette="viridis", ax=ax)
    ax.set_facecolor('lavender')
    plt.xlabel("Election Phase", fontsize=12, fontweight="bold", color="red")
    plt.ylabel("Number of Candidates", fontsize=12, fontweight="bold", color="red")
    plt.title("Phase-wise Candidate Distribution", fontsize=16, fontweight="bold", color="purple")
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle="--", alpha=0.7)
    st.pyplot(fig)

elif visualization == "State-wise Candidate Count":
    st.sidebar.header("🔍 Filters for State-wise Distribution")
    state_options = df_candidates["State"].unique()
    state_filter = st.sidebar.multiselect("Select State", ["Select All"] + list(state_options), default=state_options)

    if "Select All" in state_filter:
        state_filter = state_options

    filtered_df = df_candidates[df_candidates["State"].isin(state_filter)]
    st.write(f"### Selected Data Count: {len(filtered_df)} Candidates")

    # --- State-wise Candidate Count ---
    st.subheader("📊 State-wise Candidate Count")
    state_counts = filtered_df['State'].value_counts().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='wheat')
    sns.barplot(x=state_counts.index, y=state_counts.values, hue=state_counts.index, palette="magma", ax=ax)
    ax.set_facecolor('cornsilk')
    plt.xlabel("State", fontsize=12, fontweight="bold", color="orange")
    plt.ylabel("Number of Candidates", fontsize=12, fontweight="bold", color="orange")
    plt.title("State-wise Candidate Count", fontsize=16, fontweight="bold", color="green")
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle="--", alpha=0.7)
    st.pyplot(fig)

# New visualizations
elif visualization == "Seats Won by Each Party":
    # Count occurrences of each party
    party_counts = df_winners["Winning Party"].value_counts()

    # Plot horizontal bar chart
    fig, ax = plt.subplots(figsize=(12, 8), facecolor='grey')
    bars = ax.barh(party_counts.index, party_counts.values, color=sns.color_palette("pastel", len(party_counts)), edgecolor="black")

    # Add value labels to bars
    for bar in bars:
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, str(int(bar.get_width())), va="center", fontsize=12, fontweight="bold", color="red")

    # Customize the plot
    ax.set_facecolor('lightgray')
    plt.xlabel("Seats Won", fontsize=14, fontweight="bold", color="darkblue")
    plt.ylabel("Party", fontsize=14, fontweight="bold", color="darkblue")
    plt.title("Seats Won by Each Party", fontsize=16, fontweight="bold", color="purple")
    plt.gca().invert_yaxis()  # Highest seats at the top
    plt.grid(axis='y', linestyle="--", alpha=0.7)
    st.pyplot(fig)


elif visualization == "Party-wise Victory Rate":
    # Count total candidates fielded by each party
    total_candidates = df_candidates['Party'].value_counts()

    # Count total seats won by each party
    total_wins = df_winners['Winning Party'].value_counts()

    # Calculate victory rate
    victory_rate = (total_wins / total_candidates) * 100

    # Remove NaN values (Parties that fielded candidates but won no seats)
    victory_rate = victory_rate.dropna()

    # Sort by victory rate (descending order)
    victory_rate = victory_rate.sort_values(ascending=False)

    # Plot the bar chart
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='coral')
    bars = ax.bar(victory_rate.index, victory_rate.values, color=sns.color_palette("viridis", len(victory_rate)), edgecolor="black")


    # Customize the plot
    ax.set_facecolor('lightsalmon')
    plt.xlabel("Party", fontsize=12, fontweight="bold", color="darkblue")
    plt.ylabel("Victory Rate (%)", fontsize=12, fontweight="bold", color="darkblue")
    plt.title("Party-wise Victory Rate", fontsize=16, fontweight="bold", color="purple")
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle="--", alpha=0.7)
    st.pyplot(fig)

elif visualization == "Candidate Success by Age":
    # Winning Candidates' Age vs Their Success Rate
    df_winners['Age Group'] = pd.cut(df_winners['Age'], bins=[20, 30, 40, 50, 60, 70, 80], labels=['20-30', '30-40', '40-50', '50-60', '60-70', '70-80'])
    age_group_counts = df_winners['Age Group'].value_counts().sort_index()

    # Plot the success rates per age group
    fig, ax = plt.subplots(figsize=(9, 5),facecolor='gray')
    ax.set_facecolor('silver')
    sns.barplot(x=age_group_counts.index, y=age_group_counts.values, palette='viridis', ax=ax)
    plt.xlabel("Age Group", fontsize=12, fontweight='bold', color="green")
    plt.ylabel("Number of Successes", fontsize=12, fontweight='bold', color="green")
    plt.title("Candidate Success by Age Group", fontsize=16, fontweight="bold", color="purple")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)

elif visualization == "Gender-wise Winning Trends":
    # Count wins by gender
    gender_wins = df_winners['Gender'].value_counts()
    # Plot the results
    fig, ax = plt.subplots(figsize=(7, 5),facecolor='grey')
    ax.set_facecolor('violet')
    sns.barplot(x=gender_wins.index, y=gender_wins.values, palette='magma', ax=ax)
    ax.set_ylabel("Number of Wins", fontsize=12, fontweight="bold")
    ax.set_title("Gender-wise Winning Trends", fontsize=16, fontweight="bold")
    st.pyplot(fig)

elif visualization == "Regional result":
    north_states = ["Punjab", "Haryana", "Uttar Pradesh", "Rajasthan", "Delhi", "Himachal Pradesh", "Jammu & Kashmir",
                    "Uttarakhand"]
    south_states = ["Tamil Nadu", "Kerala", "Andhra Pradesh", "Karnataka", "Telangana"]
    east_states = ["West Bengal", "Odisha", "Jharkhand", "Bihar", "Assam"]
    west_states = ["Maharashtra", "Gujarat", "Goa", "Madhya Pradesh", "Chhattisgarh", "Rajasthan"]
    # Create a region column
    def assign_region(state):
        if state in north_states:
            return "North"
        elif state in south_states:
            return "South"
        elif state in east_states:
            return "East"
        elif state in west_states:
            return "West"
        else:
            return "Other"

    df_winners['Region'] = df_winners['State'].apply(assign_region)
    # Count winning parties in each region
    regional_party_counts = df_winners.groupby(["Region", "Winning Party"]).size().unstack().fillna(0)

    # Plot Regional Dominance
    regional_party_counts.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='Set2')
    plt.xlabel("Region", fontsize=12, fontweight="bold", color="red")
    plt.ylabel("Number of Seats Won", fontsize=12, fontweight="bold", color="red")
    plt.title("Regional Dominance of Parties (North/South/East/West)", fontsize=16, fontweight="bold", color="brown")
    plt.legend(title="Winning Party", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(axis='y', linestyle="--", alpha=0.7)
    st.pyplot(plt)

elif visualization =="Candidates Contested vs. Seats Won":
    # Assuming df_candidates and df_winners are the DataFrames containing election data for candidates and winners
    # ✅ 1. Count Total Candidates Fielded by Each Party
    party_candidates = df_candidates.groupby("Party")["Candidate Name"].count().reset_index()
    party_candidates.rename(columns={"Candidate Name": "Total Candidates"}, inplace=True)
    # ✅ 2. Count Total Seats Won by Each Party
    party_wins = df_winners.groupby("Winning Party")["State"].count().reset_index()
    party_wins.rename(columns={"State": "Seats Won", "Winning Party": "Party"}, inplace=True)
    # ✅ 3. Merge Both DataFrames to Compare
    party_performance = pd.merge(party_candidates, party_wins, on="Party", how="left").fillna(0)
    party_performance["Seats Won"] = party_performance["Seats Won"].astype(int)
    # ✅ 4. Calculate Success Rate (% of Candidates Who Won)
    party_performance["Success Rate (%)"] = (party_performance["Seats Won"] / party_performance[
        "Total Candidates"]) * 100
    # ✅ 5. Sort by Seats Won (Top 10)
    party_performance = party_performance.sort_values(by="Seats Won", ascending=False).head(10)

    fig, ax1 = plt.subplots(figsize=(12, 6), facecolor='yellow')
    bar1 = sns.barplot(x="Party", y="Total Candidates", data=party_performance, color="lightgreen",
                       label="Total Candidates", ax=ax1)
    bar2 = sns.barplot(x="Party", y="Seats Won", data=party_performance, color="orange", label="Seats Won", ax=ax1)


    ax1.set_facecolor('lightyellow')
    ax1.set_xlabel("Party", fontsize=12, fontweight="bold", color="brown")
    ax1.set_ylabel("Count", fontsize=12, fontweight="bold", color="brown")
    ax1.set_title("Candidates Contested vs. Seats Won (Top 10 Parties)", fontsize=16, fontweight="bold", color="purple")
    ax1.legend()
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle="--", alpha=0.7)
    st.pyplot(fig)

elif visualization =="Top 10 Closest Contests":
    # ✅ 1. Select Relevant Columns
    df_winners_filtered = df_winners[["State", "PC Name", "Winning Candidate", "Winning Party",
                                      "Runner-up Canddiate", "Runner-up Party", "Margin Votes"]]

    # ✅ 2. Convert Margin Votes to Numeric (If Not Already)
    df_winners_filtered = df_winners_filtered.copy()
    df_winners_filtered["Margin Votes"] = pd.to_numeric(df_winners_filtered["Margin Votes"], errors="coerce")

    # ✅ 3. Get the Top 10 Closest Contests (Smallest Margins)
    df_closest_contests = df_winners_filtered.nsmallest(10, "Margin Votes")

    # ✅ 4. Plot Smallest Winning Margins
    plt.figure(figsize=(12, 6), facecolor='chocolate')
    ax = sns.barplot(data=df_closest_contests, y="PC Name", x="Margin Votes", hue="Winning Party", dodge=False,
                     palette="twilight")
    ax.set_facecolor('peru')
    plt.xlabel("Winning Margin (Votes)", fontsize=12, fontweight="bold", color="purple")
    plt.ylabel("Constituency", fontsize=12, fontweight="bold", color="purple")
    plt.title("Top 10 Closest Contests – Smallest Winning Margins", fontsize=16, fontweight="bold", color="pink")
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.legend(title="Winning Party")
    st.pyplot(plt)

elif visualization =="Top 10 Largest Winning Margins":
    # ✅ 1. Select Relevant Columns
    df_winners_filtered = df_winners[["State", "PC Name", "Winning Candidate", "Winning Party",
                                      "Runner-up Canddiate", "Runner-up Party", "Margin Votes"]]

    # ✅ 2. Convert Margin Votes to Numeric (If Not Already)
    df_winners_filtered = df_winners_filtered.copy()
    df_winners_filtered["Margin Votes"] = pd.to_numeric(df_winners_filtered["Margin Votes"], errors="coerce")

    # ✅ 3. Get the Top 10 Largest Winning Margins
    df_landslide_wins = df_winners_filtered.nlargest(10, "Margin Votes")

    # ✅ 4. Plot Largest Winning Margins
    plt.figure(figsize=(12, 6), facecolor='springgreen')
    ax = sns.barplot(data=df_landslide_wins, y="PC Name", x="Margin Votes", hue="Winning Party", dodge=False,
                     palette="ocean_r")
    ax.set_facecolor('palegreen')
    plt.xlabel("Winning Margin (Votes)", fontsize=12, fontweight="bold", color="orange")
    plt.ylabel("Constituency", fontsize=12, fontweight="bold", color="orange")
    plt.title("Top 10 Landslide Wins – Largest Winning Margins", fontsize=16, fontweight="bold", color="blue")
    plt.grid(axis="x", linestyle="--", alpha=0.7)
    plt.legend(title="Winning Party")

    # Render plot in Streamlit
    st.pyplot(plt)
