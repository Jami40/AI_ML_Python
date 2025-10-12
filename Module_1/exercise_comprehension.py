text = "Educating AI with Python"

vowels=[ch for ch in text if ch.lower() in 'aeiou']

print("Vowels in the text:", vowels)


letter={ch for ch in text.lower() }

print("Unique letters in the text:", letter)



number={
    i:(
         'Even' if i%2==0 else 'Odd'

    )

    for i in range(6)
}

print("Number types:", number)