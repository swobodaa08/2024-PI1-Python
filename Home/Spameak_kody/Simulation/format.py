import random

def generate_stats(elo):
    elo_score = int(elo)
    norm_elo = max(800, min(elo_score, 1200))  # obmedz ELO
    scale = (norm_elo - 800) / 400  # 0 až 1

    # Počet zápasov
    total_matches = 20

    goals_scored = random.randint(int(40 + 50 * scale), int(70 + 60 * scale))
    goals_conceded = random.randint(int(50 - 30 * scale), int(60 - 40 * scale))

    # Bezpečné rozsahy
    min_win = int(5 + 8 * scale)
    max_win = int(14 + 6 * scale)
    if min_win > max_win:
        min_win = max_win

    win = random.randint(min_win, max_win)
    draw = random.randint(0, total_matches - win)
    loss = total_matches - win - draw

    yellow = random.randint(20, 50)
    red = random.randint(0, 10)

    return goals_scored, goals_conceded, yellow, red, win, loss, draw


def process_teams(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(output_file, "w", encoding="utf-8") as out:
        for line in lines:
            if not line.strip():
                continue
            name, elo = line.strip().split(",")
            goals_scored, goals_conceded, yellow, red, win, loss, draw = generate_stats(elo)
            out.write(f"Team: {name}\n")
            out.write(f"elo: {elo}\n")
            out.write(f"goals_scored: {goals_scored}\n")
            out.write(f"goals_conceded: {goals_conceded}\n")
            out.write(f"yellow: {yellow}\n")
            out.write(f"red: {red}\n")
            out.write(f"win: {win}\n")
            out.write(f"loss: {loss}\n")
            out.write(f"draw: {draw}\n\n")
            # except ValueError:
            #     print(f"Chybný riadok: {line.strip()}")

# Spustenie
process_teams("Home/Spameak_kody/Spameak_Casino/timy_futbal.txt", "Home/Spameak_kody/Simulation/teams.txt")