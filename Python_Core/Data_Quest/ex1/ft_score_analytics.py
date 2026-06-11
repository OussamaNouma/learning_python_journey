import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    size: int = len(sys.argv)
    if size > 1:
        scores: list[int] = []
        for x in range(1, size):
            try:
                scores.append(int(sys.argv[x]))
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[x]}'")

        scores_len = len(scores)
        if scores_len == 0:
            print("No scores provided. Usage: python3 "
                  "ft_score_analytics.py <score1> <score2> ...")

        else:
            my_sum: int = sum(scores)
            my_max: int = max(scores)
            my_min: int = min(scores)
            print(f"Scores processed: {scores}")
            print(f"Total players: {scores_len}")
            print(f"Total score: {my_sum}")
            print(f"Average score: {my_sum/scores_len}")
            print(f"High score: {my_max}")
            print(f"Low score: {my_min}")
            print(f"Score range: {my_max - my_min}")
    else:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
