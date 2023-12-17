#include <wchar.h>
#include <stdlib.h>

#include "struct.h"
#include "print_error.h"
#include "free_all.h"

wchar_t* sent_realloc(struct Text text, wchar_t* sent, int size){
	wchar_t* old_sent = sent;
	sent = (wchar_t*)realloc(sent, sizeof(wchar_t)*size);
	if (!sent){
		print_error(L"Недостаточно памяти для выполнения операции");
		free(old_sent);
		free_all(text);
		exit(0);
	}
	return sent;
}

void replace_symbols(struct Text txt){
	for (size_t i = 0; i < txt.len; i++){
		if (wcscspn(txt.ptr[i]->ptr, L"@#%") != txt.ptr[i]->len){
			wchar_t* sent = (wchar_t*)malloc(sizeof(wchar_t)*txt.ptr[i]->len);
			int len = txt.ptr[i]->len;
			int id = 0;
			for (int x = 0; x <= txt.ptr[i]->len; x++){
				switch (txt.ptr[i]->ptr[x]){
					case L'@':
						len += 4;
						sent = sent_realloc(txt, sent, len);
						wcscat(sent, L"(at)");
						id += 4;
						break;
					case L'#':
						len += 9;
                        sent = sent_realloc(txt, sent, len);
                        wcscat(sent, L"<решетка>");
                        id += 9;
                        break;
					case L'%':
						len += 9;
                        sent = sent_realloc(txt, sent, len);
                        wcscat(sent, L"<percent>");
                        id += 9;
                        break;
					default:
						sent[id++] = txt.ptr[i]->ptr[x];
						break;
				}
			}
			free(txt.ptr[i]->ptr);
			txt.ptr[i]->ptr = sent;
			txt.ptr[i]->len = len;
		}
	}
}
