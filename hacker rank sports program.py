if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(set(arr))  # Remove duplicates and convert to list
    scores.sort(reverse=True)  # Sort scores in descending order
    runner_up_score = scores[1]  # Second highest score
    print(runner_up_score)
