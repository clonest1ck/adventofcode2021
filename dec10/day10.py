
closers = { '(' : ')'
          , '[' : ']'
          , '{' : '}'
          , '<' : '>'
          }

validate_points = { ')' : 3
                  , ']' : 57
                  , '}' : 1197
                  , '>' : 25137
                  }

autocomplete_points = { ')' : 1
                      , ']' : 2
                      , '}' : 3
                      , '>' : 4
                      }

def validate(line):
  global closers

  expected_closers = []

  for c in line:
    if c in closers:
      expected_closers.append(closers[c])
    elif c != expected_closers.pop():
      return False, c

  return True, expected_closers 

f = open('day10.txt', 'r')

validate_score = 0
autocomplete_scores = []

for line in f:
  valid, error = validate(line.strip())

  if not valid:
    validate_score += validate_points[error]
  else:
    score = 0
    for c in reversed(error):
      score = score * 5 + autocomplete_points[c]
    autocomplete_scores.append(score)

autocomplete_score = list(sorted(autocomplete_scores))[round((len(autocomplete_scores) - 1) / 2)]

print("Part 1: %d" % validate_score)
print("Part 2: %d" % autocomplete_score)
