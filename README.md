# Goat Tools

## Purpose
This is a learning excercise. This is an attempt to recreate many common CLI tools in different languages. This aims to have a Test Driven Development focus. 

## Development Utils
* do_both - Runs your tool and the real tool at the sametime
   *  `do_both cat -n file.txt`
* goatgen - Based on [tools](tools.txt) generate details for maintaining the repo
   * `goatgen completion_report` 


# Completion Report

| test_status | test_count | status | language | name |
| ----------- | ---------- | ------ | -------- | ---- |
| True        | 3          | True   | python   | cat  |
| False       | 0          | True   | golang   | cat  |
| True        | 3          | True   | python   | tac  |


:white_check_mark:  ✅

:x: ❌