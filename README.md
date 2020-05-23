# 1. Opis projektu:
  Projekt skupia się na stworzeniu tłumaczenia pythona 3+ na polską wersję językową.
  Działanie zakłada translację polskiej wersji pythona na oryginalną, którą później uruchamia się poprzez interpreter pythona. Osiągnięta jest ona poprzez zastosowanie słowników słów kluczowych i funkcji wbudowanych zbudowanych na zasadzie: słownik["polskie tłumaczenie"]= "angielski odpowiednik". 
  Całość zorganizowana jest wokół pythona, dlatego też jest w nim zaimplementowana.

# 2. Podstawa teoretyczna do projektu:
  Język python w odróżnieniu od języków wywodzących się z ALGOL (z ang. ALGOrithmic Language) nie zawiera bloków kodu wewnątrz “{ }”, czy też struktur typu “BEGIN END” a stosuje wcięcia do ustalania logicznego przyporządkowania do bloku. Z tego względu gramatyka pythona nie jest gramatyka bezkontekstową bo polega na informacji o poprzednich poziomach wcięć. 

# 3. Opis zastosowanego rozwiązania:
  Zaproponowane rozwiązanie składa się z logicznie dwóch elementów: leksera dla polskiego pythona produkującego zbiór tokenów oraz translatora, który operując na tym zbiorze tworzy kod wynikowy pythona.
  Do tworzenia tokenów użyto biblioteki ply i jej klasy LexToken, która składa się z:
  
```python
  # Token class.  This class is used to represent the tokens produced.
  class LexToken(object):
      def __repr__(self):
          return f'LexToken({self.type},{self.value!r},{self.lineno},{self.lexpos})'
```
  
   W przypadku tłumaczonych funkcji budowanych i słów kluczowych tworzone był LexTokeny, których typem było polskie, a wartością angielski jego odpowiednik. Dla pozostałych tokenów pozostawała konwencja type: nazwa value: wartość.

## Tokeny INDENT i DEDENT:
  Tokeny są generowane na podstawie dopasowania do wyrażenia regularnego. W przypadku indentów szukamy nowej linii i dowolnej liczby spacji. Za prawidłowy indent uważamy 4 spacje. W przypadku gdy ilość spacji jest niepodzielne przez 4 to zwracane zostaje None. Do śledzenia ilości występujących indentów używamy stosu. Na podstawie informacji przechowywanych na stosie, decydujemy, czy wygenerować następny indent, nie generować nic ( tylko NEWLINE) lub wygenerować odpowiednią liczbę dedentów oraz aktualizujemy aktualny stan wcięcia na stosie.

  Zrezygnowaliśmy z napisania parsera(do sprawdzania poprawności kodu po stronie kodu napisanego w plpy) ze względu na napotkane trudności, w trakcie implementacji okazało się, że to zadanie przerasta nasze możliwości ze względu na to, że gramatyka pythona nie jest gramatyka bezkontekstową (INDENT i DEDENT zależą od poprzedniej linii programu), przez co nie mogliśmy użyć np narzędzia yacc do stworzenia parsera. A napisanie od podstaw całego parsera dla wszystkich lex-tokenów występujących w pythonie byłoby bardzo trudne. W rezultacie w przypadku błędu otrzymujemy krótką informację o powodzie błędu po angielsku i numer linii w której jest problem. 

# 4. Przykłady użycia:

  Szybkie sortowanie - implementacja quicksorta i użycie go na przykładowej tablicy. Sposób uruchomienia z katalogu głównego:
python plpy.py przyklady/szybkie_sortowanie.plpy

  Wąż - prosta gra napisana przy użyciu biblioteki pygame, pokazująca że w kodzie napisanym w plpy da się używać zewnętrznych bibliotek. Sposób uruchomienia z katalogu głównego:
python plpy.py przyklady/waz.plpy

# 5. Podział prac:
- słowniki słów kluczowych, funkcji wbudowanych: **Maciej Wilk**
- lekser, bez obsługi IDENT i DEDENT: **Maciej Wilk**
- tokeny dla IDENT i DEDENT: **Sonia Radoń**
- próba tworzenia parsera: **Robert Czarnik**
- translator na pythona: **Ewa Tabor, Maciej Wilk** (push na Gita od Maciej Wilk)
-  spięcie w pojedyncze wywołanie: **Sonia Radoń**
- przykłady użycia: **Robert Czarnik**
- dodanie obsługi komentarzy: **Ewa Tabor**
- poprawa obsługi string do działania na multiline: **Ewa Tabor**

link do doku: 
https://docs.google.com/document/d/14pQ0l4JekJbRhlgCLPLwhurmKZyAOBoZagdd3VvZrB8/edit?usp=sharing
