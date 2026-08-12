import sys

from predict import predict

if len(sys.argv) < 2:
    print("Bruk: python main.py <bilde>")
    quit()

results = predict(sys.argv[1])

print("\nTopp 3 prediksjoner:\n")

for i, (pokemon, confidence) in enumerate(results, start=1):
    print(f"{i}. {pokemon}: {confidence:.2f}%")