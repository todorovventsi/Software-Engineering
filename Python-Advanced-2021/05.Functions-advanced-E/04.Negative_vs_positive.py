def compare_negatives_with_positives(nums):
    positives = sum(filter(lambda x: x > 0, nums))
    negatives = sum(filter(lambda x: x < 0, nums))
    print(negatives)
    print(positives)
    if positives > abs(negatives):
        return "The positives are stronger than the negatives"
    return "The negatives are stronger than the positives"


numbers = [int(num) for num in input().split()]
print(compare_negatives_with_positives(numbers))
