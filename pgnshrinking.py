import chess.pgn

n = 100000 # Change this variable to number of games you want to shrink.

in_path = "lichess.pgn" # Name of initial pgn file
out_path = "chessgames.pgn" # Name of output pgn file

with open(in_path, encoding="utf-8") as pgn_in, open(out_path, "w", encoding="utf-8") as pgn_out:
    for i in range(n):  # shrink to first "n" games in the pgn
        game = chess.pgn.read_game(pgn_in)
        if game is None:
            break
        pgn_out.write(str(game) + "\n\n")  
    
print("Sucessfully shrinked to {i+1} games and saved to '{out_path}'")
