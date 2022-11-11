README placeholder

Thoughts to flesh out later:
- data comes before identification in modules because it's more commonly a required field since more than one type of identification is typical
- With deprecated assets like peripherals and managed preferences the get, update, and delete endpoints will be added but not creation since you shouldn't be making these anymore but you may still want to have access to disable or delete them since they're not in the GUI anymore
- Get module that end in a plural return all values or filtered selection of all values that return in the same data format as the all request. The only exception to this is if the singular and plural word for the end of the endpoint name is the same (like software) then the all request is appended with _all to differentiate it
- The module names reflect the get, create, update, delete privilege requirements because they're more readable and easier to understand than post and put for people that aren't familiar with working with HTTP requests