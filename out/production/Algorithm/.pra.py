def count_abc_occurrences_in_file(file_path):
    count = 0
    search_str = '<div class="flex-1 text-ellipsis max-h-5 overflow-hidden break-all relative">'
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            start = 0
            while start < len(line):
                start = line.find(search_str, start)
                if start == -1:
                    break
                count += 1
                start += len(search_str)

    return count

file_path = "gpt.txt"
result = count_abc_occurrences_in_file(file_path)
print("파일 안에 특정 키워드가 {}번 등장했습니다.".format(result))