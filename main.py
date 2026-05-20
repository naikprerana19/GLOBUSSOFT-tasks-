from deepface import DeepFace

# Compare two images
result = DeepFace.verify(
    img1_path="py1.jpg",
    img2_path="py2.jpg"
)

# Print result
if result["verified"]:
    print("Same Person")
else:
    print("Different Persons")