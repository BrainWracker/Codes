#pragma once
#include <wchar.h>

struct Sentence{
	wchar_t* ptr;
	int cnt;
	int len;
};


struct Text{
	struct Sentence** ptr;
	int len;
};
