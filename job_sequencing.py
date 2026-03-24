def schedule_jobs(jobs, deadlines, profits):
    n = len(jobs)
    order = sorted(zip(profits, deadlines, jobs), key=lambda x: -x[0])
    max_deadline = max(deadlines)
    result = [None] * max_deadline
    total_profit = 0
    for profit, d, job in order:
        for slot in range(min(max_deadline, d) - 1, -1, -1):
            if result[slot] is None:
                result[slot] = job
                total_profit += profit
                break
    return [j for j in result if j is not None], total_profit

if __name__ == "__main__":
    jobs, deadlines, profits = ['j1', 'j2', 'j3', 'j4', 'j5'], [2, 1, 2, 1, 3], [100, 19, 27, 25, 15]
    schedule, profit = schedule_jobs(jobs, deadlines, profits)
    print("Scheduled jobs:", schedule)
    print("Total profit:", profit)
