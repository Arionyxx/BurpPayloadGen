# Burp Suite Payload Generator

A simple Python tool to generate payloads for Burp Suite testing.

## Features

### 1. Number Generator
Generate sequential numbers from a starting point to an ending point.
- Example: Generate numbers from 100 to 700
- Output: Each number on a new line
- Use case: Testing numerical parameters, IDs, question numbers, etc.

### 2. Username Generator
Generate random usernames from predefined templates.
- Creates variations like: FemboyHotie, Assassin2000, PWNED, Hacked666, etc.
- Customizable count
- Use case: Testing authentication, user enumeration, brute force, etc.

### 3. Message Generator
Generate security warning messages.
- Predefined vulnerability messages
- Professional security notifications
- Use case: Testing input validation, message handling, XSS testing, etc.

### 4. Event Type Generator
Generate custom vulnerability-themed event type payloads.
- Custom security event names (vulnerabilityAlert, vulnFound, securityBreach, dataLeak, etc.)
- 10 unique vulnerability-themed event types for security testing
- Use case: Testing custom event handlers, XSS via event attributes, JavaScript injection, security event testing, etc.

## Requirements

- Python 3.x
- No external dependencies required

## Usage

1. Run the script:
```
python burp_payload_generator.py
```

2. Select from the menu:
   - Press `1` for Number Generator
   - Press `2` for Username Generator
   - Press `3` for Message Generator
   - Press `4` for Event Type Generator
   - Press `5` to Exit

3. Follow the prompts to generate your payload files

4. Use the generated `.txt` files in Burp Suite Intruder

## Examples

### Number Generator
```
Enter starting number: 100
Enter ending number: 700
Enter output filename (default: numbers.txt): question_ids.txt

✅ Generated 601 numbers in 'question_ids.txt'
```

### Username Generator
```
How many usernames to generate? 50
Enter output filename (default: usernames.txt): usernames.txt

✅ Generated 50 usernames in 'usernames.txt'
```

### Message Generator
```
Enter output filename (default: messages.txt): messages.txt

✅ Generated 25 messages in 'messages.txt'
```

### Event Type Generator
```
Enter output filename (default: event_types.txt): event_types.txt

✅ Generated 10 event types in 'event_types.txt'
```

## Output Files

All generated files are plain text files with one entry per line, perfect for loading into Burp Suite Intruder:

- `numbers.txt` - Sequential numbers (one per line)
- `usernames.txt` - Random usernames (one per line)
- `messages.txt` - Security warning messages (one per line)
- `event_types.txt` - Event type strings (one per line)

## How to Use in Burp Suite

1. Open Burp Suite
2. Send a request to Intruder
3. Mark your injection points
4. Go to Payloads tab
5. Click "Load" and select your generated `.txt` file
6. Start the attack

## Customization

You can easily modify the script to add:
- More username templates in the `base_names` list
- More suffixes in the `suffixes` list
- More security messages in the `messages` list
- More event types in the `event_types` list

Enjoy testing! 🔥
