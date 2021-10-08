from indeed import extract_indeed_jobs, extract_indeed_pages

# #range - 입력한 수 만큼의 크기의 배열을 생성
# for n in range(max_page):
#     print(f"start={n*50}")

last_indeed_pages = extract_indeed_pages()

extract_indeed_jobs(last_indeed_pages)
