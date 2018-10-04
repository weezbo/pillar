# PillarTechnology-babysitter-kata

Code kata by Maxwell Muir

This is my response for a code kata found here: [babysitter kata](https://github.com/PillarTechnology/kata-babysitter)

Additionally, after choosing the kata and requesting more information, I was advised of the following:
- Time inputs can be integers representing whole hours rather than time/datetime objects or strings.
- Time integers would be the hour values on a 24 hour clock.
- No interface was required for the scope of the kata.
- Bedtimes could be optional or could occur after midnight, in which case the higher post-midnight rate applies.
- I inferred that bedtimes could also precede start times, in which case the lower post bedtime rate would apply to the entire pre-midnight period.


## Technology 

This class was built in Python version 3.4.3 and uses standard libraries (unittest is imported for babysitter_test.py). Having this Python version in your environment is required for running.

## Installation/Running

Once the repository is cloned to a directory, the unit tests can be run from command line in that directory with the command:

 `python3 -m unittest babysitter_test.py`

If you would like to use the Babysitter class in a different project, it will need to be imported within your code with:
`from babysitter import Babysitter`
and create a babysitter object with:
`<object_name> = Babysitter()`

From there, `Babysitter.calculatePay()` accepts two or three parameters, all integers: start time for shift, end time for shift, and bedtime. Bedtime is optional and will default to False if no bedtime is provided. `Babysitter.calculatePay()`  returns an integer value representing the total wage for the shift.


## A Commentary on Limitations and Suggestions for Future Improvement
Babysitter is designed for an environment which already has an interface and converter to turn times into integers and it returns an integer value for the total. This covers the current requirements but leaves some room for future improvement. The main things I see for consideration are:
- Add getters and setters for the start minimum time and end maximum time.
- Add getters and setters for the rates for each time period (pre-bedtime, post-bedtime, and post-midnight).
- Switch to handling of decimals for rates.
- Possible "nap time" handling if the shift starts during a nap and has a period of wakefulness before bedtime.
