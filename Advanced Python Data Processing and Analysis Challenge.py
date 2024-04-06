#Question 3
#Task 1
import re

positive_words_pattern= r"\b(amazing|wonderful|relaxed|breathtaking|unique|stunning)\b"
negative_words_pattern = r"\b(bad|disappointing|poor|overcrowded|lackluster|scarce)\b"
positive_words= []
negative_words=[]
with open('travel_blog.txt', 'r') as file:
    #print(file.read())
    for line in file:
        positive_word=re.findall(positive_words_pattern, line, re.IGNORECASE)
        negative_word=re.findall(negative_words_pattern, line, re.IGNORECASE)
        if positive_word:
            positive_words += positive_word
        if negative_word:
            negative_words += negative_word

print(f'\nThe positive words found in the travel blog were: {', '.join(set(positive_words))}') 
print(f"\nThere were {len(positive_words)} occurences of positive word(s) in the travel blog.")
print(f'\nThe negative words found in the travel blog were: {', '.join(set(negative_words))}')
print(f"\nThere were {len(negative_words)} occurences of negative word(s) in the travel blog.\n")

#Task 2
pattern= r',(\d+)'
file1_sum = 0
file1_days = 0
file2_sum = 0
file2_days = 0
with open('weather_2020.txt', 'r') as file1, open('weather_2021.txt', 'r') as file2:
    
    for day in file1:
        file1_days += 1
        temp = re.search(pattern, day)
        file1_sum += int(temp.group(1))
        
        
    
    for day in file2:
        file2_days += 1
        temp = re.search(pattern, day)
        file2_sum += int(temp.group(1))
        
    

year1_avg= file1_sum/file1_days
year2_avg=file2_sum/file2_days
    
print(f"{round(year1_avg, 2)}")
print(f"{round(year2_avg, 2)}")
print(f"The year 2020 has the highest average" if year1_avg > year2_avg else f"The year 2021 has the highest average." )