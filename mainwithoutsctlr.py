import pandas as pd
from rapidfuzz import fuzz
from multiprocessing import Pool, cpu_count

# Step 2: Fuzzy match within filtered candidates using parallel processing
def fuzzy_match_row(args):
    row, candidates = args
    best_score = 0
    best_match = ("No match found", "No match found", "No date found")  # Default response

    for _, candidate in candidates.iterrows():
        # Use token set ratio to find potential name matches
        score = fuzz.token_set_ratio(row['full_name'], candidate['full_name'])

        # Check for a high score (above threshold) and if date matches
        if score > 80:
            if row['Date Naissance'] == candidate['Date Naissance']:  # Check if dates match
                return (candidate['C'], candidate['D'], candidate['Date Naissance'])  # Perfect match found

        # Update best match if this candidate has a better score
        if score > best_score:
            best_score = score
            best_match = (candidate['C'], candidate['D'], candidate['Date Naissance'])

    return best_match

# Main function to load data, process it, and save results
def main():
    # Load data from Excel into pandas DataFrames
    df1 = pd.read_excel("EFFECTIF.xlsx", sheet_name="sheet1")
    df2 = pd.read_excel("EFFECTIF.xlsx", sheet_name="Sheet2")

    # Concatenate names and prénoms for matching
    df1['full_name'] = df1['C'] + ' ' + df1['D']
    df2['full_name'] = df2['C'] + ' ' + df2['D']

    # Ensure 'full_name' columns are strings (in case of NaN or other non-string types)
    df1['full_name'] = df1['full_name'].astype(str)
    df2['full_name'] = df2['full_name'].astype(str)

    # Step 1: Pre-filter potential matches with high token set ratio
    cosine_threshold = 80  # Similarity threshold
    potential_matches = []

    for i, row in df1.iterrows():
        row_candidates = df2[df2['full_name'].apply(lambda x: fuzz.token_set_ratio(row['full_name'], x)) >= cosine_threshold]
        potential_matches.append(row_candidates)

    # Prepare inputs for parallel processing
    input_data = [(df1.iloc[i], potential_matches[i]) for i in range(len(df1))]

    # Use multiprocessing Pool for parallel fuzzy matching
    with Pool(cpu_count()) as pool:
        results = pool.map(fuzzy_match_row, input_data)

    # Write the results back to df1
    df1[['J', 'K', 'Date']] = pd.DataFrame(results, columns=['J', 'K', 'Date'])  # Include Date

    # Save results to Excel
    df1.to_excel("yourfile_results.xlsx", sheet_name="Sheet1", index=False)

# This will make sure the code runs only when the script is executed, not when it is imported
if __name__ == '__main__':
    main()
