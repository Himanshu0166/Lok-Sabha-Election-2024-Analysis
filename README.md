#### app.py is a Streamlit verson 
[Click here to visit my deployed app](https://lok-sabha-election-2024-analysis.streamlit.app/)

# Lok-Sabha-Election-2024-Analysis

LOK SABHA ELECTION(2024) ANALYSIS

📌 Election Data Analysis 

This program loads and analyzes election-related datasets using Pandas, Matplotlib, and Seaborn.

It imports data from three Excel files:
•	candidates_with_phase.xlsx: Contains information about candidates and election phases.
•	result.xlsx: Includes election results for all candidates.
•	result_winner.xlsx: Lists the winners of the election.

The program reads these datasets into Pandas DataFrames and displays the first few rows of each for initial inspection.
The dataset used in this analysis is sourced from Kaggle. You can download it from the following link:
Download the dataset from Kaggle

📌 Gender Distribution of Candidates¶

This visualization displays the gender distribution of candidates in the Lok Sabha 2024 elections.
The dataset is analyzed using Pandas, and the count plot is created using Seaborn with customized aesthetics.

Key Features of the Visualization:
•	Seaborn's whitegrid style is used for a clean and structured appearance.
•	Count plot represents the number of male and female candidates.
•	Color customization using the 'viridis' palette for better contrast.
•	Edge highlighting and data labels on bars to enhance readability.
•	Custom title, axis labels, and grid styling for better visualization.

This chart helps in understanding the gender representation among the candidates.

📌 Age Distribution of Candidates¶

This visualization represents the age distribution of candidates in the Lok Sabha 2024 elections.
The histogram provides insights into the spread and concentration of candidate ages, helping identify common age groups.

Key Features of the Visualization:
•	Histogram with KDE (Kernel Density Estimation): Displays the age distribution along with a smooth density curve for better analysis.
•	Seaborn's darkgrid style: Enhances readability with a subtle background grid.
•	Customized aesthetics:
	Color: Blue histogram (#1f77b4) with a purple KDE curve for contrast.
	Transparency (alpha=0.8): Ensures a sleek look.
	Black edge color for bars with increased linewidth for clarity.
•	Annotations on bars: Displays the count of candidates in each bin.
•	Title and labels: Styled with custom font size, weight, and colors.
•	Gridlines and ticks: Improve readability while maintaining a clean layout.

This plot helps in understanding the age demographics of the candidates, showing which age groups have higher representation in the elections.

📌 Phase-wise Candidate Distribution

This visualization represents the number of candidates participating in each election phase of the Lok Sabha Election 2024.
🔍 Steps in Analysis:
•	Count Distribution – The number of candidates in each phase is calculated using value_counts() and sorted in order.
•	Data Display – The phase-wise candidate count is printed for reference.
•	Visualization – A bar chart is created using Seaborn to represent the candidate distribution across phases.
•	Customization – Labels, gridlines, and color palettes are adjusted for better readability.

📊 Insights:
•	Helps in understanding how candidates are distributed across different election phases.
•	Provides a quick overview of participation trends throughout the election process. 🚀

📌 State-wise Candidate Distribution

This analysis examines the number of candidates contesting from each state in the Lok Sabha Election 2024.

🔹 Steps Performed:
1.	Counts the Number of Candidates per State
•	Uses value_counts() to determine the number of candidates from each state.
•	Sorts the values in descending order to highlight states with the highest participation.
2.	Visualizes the Distribution Using a Bar Plot
•	Creates a bar chart using seaborn.barplot().
•	Uses the 'magma' color palette for an enhanced visual effect.
•	Assigns hue based on the state for better differentiation.
3.	Customizes the Plot for Readability
•	Adds titles and labels to ensure clarity.
•	Rotates x-axis labels (90°) to properly display state names.
•	Adds grid lines (-- style) to improve readability.

📊 Purpose

This visualization helps in understanding the distribution of candidates across different states in the 2024 Lok Sabha elections and highlights key participation trends.

📌 Seats Won by Each Party¶
This visualization presents a horizontal bar chart displaying the number of seats won by each political party in the Lok Sabha 2024 elections.

Key Features of the Visualization:
•	Bar Chart (Horizontal): Helps in better readability, especially when comparing multiple categories.
•	Dynamic Color Palette: Uses Seaborn's "pastel" color scheme for enhanced visual appeal.
•	Value Labels on Bars: Displays the number of seats won by each party for quick insights.
•	Title and Labels:
	X-axis ("Seats Won") and Y-axis ("Party") labeled with bold, colored fonts.
	Chart title ("Seats Won by Each Party") styled in purple for emphasis.
•	Inverted Y-Axis: Ensures that the party with the highest seats appears at the top for better interpretation.
•	Edge Colors for Bars: Black outlines for better differentiation between bars.
This plot helps in understanding the distribution of seats among different parties, making it easy to compare their performance in the elections.

📌 State-wise Winning Party Trends

This analysis focuses on state-wise trends by visualizing the number of seats won by the top 5 political parties (excluding Independent candidates) in the 2024 Lok Sabha elections.

🔹 Steps Performed:
1.	Excludes Independent Candidates
•	Filters out candidates labeled as "Independent" from the dataset.
2.	Identifies the Top 5 Winning Parties
•	Counts the total seats won by each party.
•	Selects the top 5 parties based on the highest number of seats won.
3.	Analyzes State-wise Party Wins
•	Groups data by State and Party to count the number of seats won per party in each state.
•	Creates a pivot table (unstacked) to prepare data for visualization.
4.	Visualizes the Data Using a Stacked Bar Chart
•	Uses a stacked bar plot to represent state-wise party dominance.
•	Applies the "tab10" colormap for clear differentiation.
5.	Enhances Readability
•	Customizes labels, titles, and gridlines for better clarity.
•	Rotates state labels (90°) to prevent overlap.
•	Positions the legend outside the plot for better visibility.

📊 Purpose

This visualization helps in understanding the regional strongholds of major political parties and how the seat distribution varies across states in the 2024 elections.

📌 📊 Party-wise Victory Rate¶
This analysis calculates and visualizes the victory rate of political parties .

📌 Insight
This plot helps in understanding which parties had the highest success rate in converting nominations into victories.

📌 📊 Election Results Analysis: Age, Gender & Regional Trends
This block analyzes election results based on three key factors: age, gender, and regional dominance of winning candidates.
________________________________________
📌 📊Insight
Identifies which age group has the most successful candidates.
________________________________________
Reveals the gender representation in election victories.
________________________________________
Highlights which political parties dominate in different regions of India.
________________________________________
📌 🎯 Key Takeaways

✅ Helps understand age trends in winning candidates.
✅ Shows gender-wise electoral success.
✅ Provides insights into regional party performance.

This analysis can be useful for political strategy, election studies, and voter behavior analysis. 🚀

📌 🗳️ Analysis of Party Performance¶

This analysis examines the performance of political parties in the Lok Sabha Election 2024, comparing the number of candidates they fielded with the seats they won. The insights help evaluate the success rate of each party.
________________________________________
•	This metric indicates how efficient each party was in converting contested seats into victories.
________________________________________

📌 📊Insight

•	A higher number of contested candidates does not always translate into more wins.
•	Some parties have a high success rate, meaning they strategically contested and secured victories efficiently.
________________________________________

📌 🔍 Conclusion

This analysis provides a quantitative overview of how political parties performed in Lok Sabha Election 2024. The success rate metric helps assess which parties were more effective in winning seats relative to the number of candidates they fielded.

📌 Analysis of Closest Contest¶

🔍 Key Insights
•	The closest contests often occur in highly competitive seats.
•	Even a few hundred votes can decide a parliamentary seat!
•	This analysis helps in understanding swing constituencies where minor shifts can impact election outcomes.

📊 Analysis of Landslide Wins

🔍 Key Insights
•	Landslide victories often indicate strong party dominance in certain regions.
•	Winning candidates in these seats had a massive lead over their opponents.
•	Helps in understanding safe seats where parties have a strong voter base.



