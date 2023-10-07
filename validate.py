import json
import sys

ERROR_FLAG_MISSING_TRANSLATION = 1
ERROR_FLAG_EMPTY_TRANSLATION = 2
ERROR_FLAG_EXTRA_TRANSLATION = 3

CONSOLE_COLOR_ERROR = '\033[31m'
CONSOLE_COLOR_RESET = '\033[0m'

required_phrases = ['New Game', 'Publisher Deals', 'Game Contracts', 'Topic and Genre', 'Topic', 'Genre',
                    'Game Size', 'Royalties', 'Penalty', 'Up-front Pay', 'No License', 'Money', 'Payroll',
                    'Games', 'Consoles', 'Weekly', 'Monthly', 'Annually', 'Level', 'No Specialization', 'Energy',
                    'Game History', 'Game Info', 'Development', 'Current Engine', 'No Engine', 'Dialogues',
                    'Statistics', 'Units Sold', 'Costs', 'Revenue', 'Released', 'Top Sales Rank', 'Platforms',
                    'Stage', 'Stage 1', 'Stage 2', 'Stage 3', 'Time Allocation', 'Features', 'Cost', 'Overall Score',
                    'Cost to Make', 'Fans Gained', 'Time', 'Pay', 'Salary', 'Info & Stats', 'Generate Report',
                    'Dev. Cost', 'License Cost', 'Market Share', 'Rating', 'Profit',
                    'Need to generate a report first.', 'Time has elapsed to generate a report.', 'Insights',
                    'Engine Development', 'Budget', 'Select Staff', 'Choose Engine', 'Develop Expansion Pack',
                    'Y{0}', 'Y{0} M{1}']


def run_test():
    with open('tagmod-translations.json', encoding='utf-8-sig') as f:
        translations = json.load(f)
        error_flag = 0
        value_string = "['"
        for language, value_holder in translations.items():
            print(f'CHECKING LANGUAGE: {language}')
            values = value_holder['values']
            provided_phrases = []
            for translation_pair in values:
                phrase = translation_pair['value']
                translation = translation_pair['translation']

                provided_phrases.append(phrase)
                new_flag = check_translation(phrase, translation)
                error_flag = new_flag if new_flag != 0 else error_flag

            new_flag = check_missing_translations(provided_phrases)
            error_flag = new_flag if new_flag != 0 else error_flag
            print('DONE')
            print()

        return error_flag


def check_translation(phrase, translation):
    error_flag = 0
    if len(translation) == 0:
        error_flag = ERROR_FLAG_EMPTY_TRANSLATION
        print(f'{CONSOLE_COLOR_ERROR}Phrase \'{phrase}\' has an empty translation.{CONSOLE_COLOR_RESET}')

    return error_flag


def check_missing_translations(provided_phrases):
    error_flag = 0
    for required_phrase in required_phrases:
        if required_phrase not in provided_phrases:
            error_flag = ERROR_FLAG_MISSING_TRANSLATION
            print(f'{CONSOLE_COLOR_ERROR}Phrase \'{required_phrase}\' is missing.{CONSOLE_COLOR_RESET}')

    for provided_phrase in provided_phrases:
        if provided_phrase not in required_phrases:
            error_flag = ERROR_FLAG_EXTRA_TRANSLATION
            print(f'{CONSOLE_COLOR_ERROR}Extra phrase \'{provided_phrase}\' provided.{CONSOLE_COLOR_RESET}')

    return error_flag


sys.exit(run_test())
