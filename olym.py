import re
import pandas as pd

def normalize_answer(x):
    try:
        # Standard modulo 1000 logic
        return int(round(float(x))) % 1000
    except:
        return 0

def my_predict(problem):
    text = str(problem).lower()
    
    # FIX: We find all digits but DON'T include the '-' in the regex.
    # This prevents '1-1' from being read as '1' and '-1'.
    numbers = [float(n) for n in re.findall(r'\d+\.?\d*', text)]

    if not numbers:
        return 0

    # Rule 1: Algebra (Solve for x)
    # Solve 4 + x = 4 -> numbers are [4, 4]. Result = 4 - 4 = 0
    if "x" in text and "=" in text and len(numbers) >= 2:
        return normalize_answer(numbers[1] - numbers[0])

    # Rule 2: Subtraction / Difference
    # Now that numbers are [1, 1], 1 - 1 = 0
    if "-" in text or "difference" in text or "minus" in text:
        if len(numbers) >= 2:
            return normalize_answer(numbers[0] - numbers[1])

    # Rule 3: Multiplication
    if any(k in text for k in ["product", "times", "\\times", "*"]):
        result = 1
        for n in numbers:
            result *= n
        return normalize_answer(result)

    # Rule 4: Addition / Sum
    if any(k in text for k in ["sum", "total", "+"]):
        return normalize_answer(sum(numbers))
    
    # Fallback
    return normalize_answer(numbers[0])

# ----------------------------
# Data Processing Block
# ----------------------------
try:
    # Use your specific path
    test_df = pd.read_csv("data/test.csv")
    
    pred_df = pd.DataFrame({
        'id': test_df['id'].astype(str),
        'answer': test_df['problem'].apply(my_predict).astype('int64'),
    })

    pred_df.to_csv("submission.csv", index=False)
    print("Predictions saved to submission.csv")
    print(pred_df)

except FileNotFoundError:
    print("Error: data/test.csv not found.")