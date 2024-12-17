from imagededup.methods import PHash

# Initialize the hashing method
phasher = PHash()

# Provide the paths to your images
image1_path = 'widget-01.png'
image2_path = 'test/widget-sample.png'

# Generate hashes for both images
hash1 = phasher.encode_image(image_file=image1_path)
hash2 = phasher.encode_image(image_file=image2_path)

# Calculate the Hamming distance between the two hashes
distance = phasher.hamming_distance(hash1, hash2)

# Print similarity score
print(f"Hamming distance between the two images: {distance}")

# Interpret the similarity
if distance == 0:
    print("The images are identical!")
elif distance < 10:  # Adjust threshold as needed
    print("The images are very similar.")
else:
    raise Exception("The result is NOT the same as expected. Please check matplotlib version.")

