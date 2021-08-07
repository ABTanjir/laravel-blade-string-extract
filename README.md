# Laravel Blade String Extract

We often start a small project and eventually it grows bigger.
And before handover clients want a last tiny-miny changes like language support. 😐

You have used proper format when using strings ```{{ __('Your String In Blade File') }}```
but now you have to browse 100 of files and extract list them to create language files.
Well... It happened to me and tried to minimize the effort a little bit and though to share this with others.

# When to use
- You have a project with lots of blade files.
- You have used ___() underscores function for printing strings.
- Now you need to add translation support and you are lazy to browse all files and collect the strings.

# How to use
1. Clone the repo
2. Install the dependencies
3. Copy all view files and folder/s from your laravel project to php folder
4. run `python extract.py`
5. You will get all your strings to `strings.blade.php`

# Cons:
You should underscored when ever you use a string  ```{{ __('Your String In Blade File') }}```
otherwise it can not extract the strings

