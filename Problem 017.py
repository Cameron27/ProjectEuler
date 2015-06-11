numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
teens = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
others = ['Hundred', 'Thousand', 'and']

answer = 0
answer += sum([len(a) for a in numbers]) * 9 * 10
answer += sum([len(b) for b in teens]) * 10
answer += sum([len(c) for c in tens]) * 10 * 10
answer -= len(tens[0]) * 9 * 10
answer += (sum([len(d) for d in numbers]) + (len(others[0]) + len(others[2])) * 9) * 100
answer -= len(others[2]) * 9
answer += len(others[1]) + len(numbers[0])
print(answer)
