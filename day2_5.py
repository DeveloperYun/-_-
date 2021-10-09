from indeed import get_jobs as get_indeed_jobs
from stack_over_flow import get_jobs as get_so_jobs

# #range - 입력한 수 만큼의 크기의 배열을 생성
# for n in range(max_page):
#     print(f"start={n*50}")

# last_indeed_pages = extract_indeed_pages()

# indeed_jobs = extract_indeed_jobs(last_indeed_pages)

indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()