#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	return len([None for chr in text if chr.isalnum()])

def get_word_length_histogram(text):
	histogram = [0]
	for word in text.split():
		length = get_num_letters(word)
		if length >= len(histogram):
			histogram += [0] * (length - len(histogram) + 1)
		histogram[length] += int(length != 0)
	return histogram

def format_histogram(histogram):
	ROW_CHAR = "*"

	number_alignment = len(str(len(histogram) - 1))
	result = "\n".join([f"{i+1 : >{number_alignment}} {ROW_CHAR * elem}" for i, elem in enumerate(histogram[1:])])
	return result

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	max_length = max(histogram)
	result = ""
	for row in range(max_length, 0, -1):
		for elem in histogram[1:]:
			result += BLOCK_CHAR if elem >= row else " "
		result += "\n"
	result += LINE_CHAR * len(histogram)
	return result


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
