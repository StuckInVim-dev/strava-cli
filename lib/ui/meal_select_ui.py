import urwid


class QuizApp:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data
        self.answers = []
        self.body = []
        self.question_widgets = []

        self.setup_ui()

    def setup_ui(self):
        # Quiz title
        self.body.append(urwid.Text(
            ('header', self.quiz_data['title']), align='center'))
        self.body.append(urwid.Divider())

        for idx, q in enumerate(self.quiz_data['questions']):
            # Determine if the question is locked
            is_locked = not q.get('locked', True)

            # Question heading
            if is_locked:
                question_text = urwid.Text(q['question'])
            else:
                question_text = urwid.Text(('locked', q['question']))
            self.body.append(question_text)

            # Store checkboxes for the options
            option_checkboxes = []

            # Create checkboxes for options
            options = q['options']
            for opt_idx, option in enumerate(options):
                # Check if 'default' key exists and set default selection accordingly
                is_default = (opt_idx == q['default']
                              ) if 'default' in q else False

                # Create checkbox
                if is_locked:
                    checkbox = MyCheckBox(option['text'], state=is_default)
                else:
                    # For locked questions, use a disabled checkbox
                    checkbox = DisabledCheckBox(
                        option['text'], state=is_default)

                # When a checkbox state changes
                if is_locked:
                    def on_state_change(button, new_state, checkboxes=option_checkboxes):
                        if new_state:
                            # Deselect other checkboxes
                            for cb_dict in checkboxes:
                                cb = cb_dict['checkbox']
                                if cb is not button and cb.state:
                                    cb.set_state(False, do_callback=False)
                        else:
                            pass  # Allow deselection of all options

                    urwid.connect_signal(checkbox, 'change', on_state_change)

                option_checkboxes.append(
                    {'checkbox': checkbox, 'option_id': option['id']})
                # Apply 'locked' attribute to styling if necessary
                if is_locked:
                    self.body.append(urwid.Padding(checkbox, left=4))
                else:
                    self.body.append(urwid.Padding(
                        urwid.AttrWrap(checkbox, 'locked'), left=4))

            self.body.append(urwid.Divider())

            # Store the default answer ID
            if 'default' in q:
                default_option_index = q['default']
                default_answer_id = q['options'][default_option_index]['id']
            else:
                default_answer_id = None

            # Store the checkboxes for the question to manage state
            self.question_widgets.append({
                'question_id': q['id'],
                'question_text': q['question'],
                'option_checkboxes': option_checkboxes,
                'locked': is_locked,
                'default_answer_id': default_answer_id
            })

        # Add a submit button at the bottom
        submit_button = urwid.Button('Submit')
        urwid.connect_signal(submit_button, 'click',
                             lambda button: self.submit_quiz())
        self.body.append(urwid.Padding(
            submit_button, align='center', width=('relative', 20)))
        self.body.append(urwid.Divider())

        # Define palette for styling
        self.palette = [
            ('header', 'bold', ''),
            ('locked', 'dark gray', '')
        ]

    def run(self):
        self.main_loop = urwid.MainLoop(
            urwid.ListBox(urwid.SimpleFocusListWalker(self.body)),
            palette=self.palette,
            unhandled_input=self.handle_input
        )
        self.main_loop.run()

    def handle_input(self, key):
        if key == 'enter':
            self.submit_quiz()

    def submit_quiz(self):
        # Collect answers
        self.answers = []
        for q in self.question_widgets:
            selected_option_id = None
            for opt in q['option_checkboxes']:
                checkbox = opt['checkbox']
                option_id = opt['option_id']
                if checkbox.state:
                    selected_option_id = option_id
                    break
            self.answers.append({
                'question_id': q['question_id'],
                'default_answer_id': q['default_answer_id'],
                'answer_id': selected_option_id
            })
        raise urwid.ExitMainLoop()


class MyCheckBox(urwid.CheckBox):
    def keypress(self, size, key):
        if key == 'enter':
            return key  # Ignore the Enter key to prevent toggling
        else:
            return super().keypress(size, key)


class DisabledCheckBox(urwid.CheckBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._selectable = False  # Make it non-selectable

    def selectable(self):
        return False  # Ensure it's not selectable

    def keypress(self, size, key):
        return key  # Ignore all keypresses


def main(quiz_data):
    app = QuizApp(quiz_data)
    app.run()
    return app.answers


if __name__ == '__main__':
    # Sample quiz dictionary with IDs, 'locked' attribute, and without default selections
    quiz = {
        'title': 'Sample Quiz',
        'questions': [
            {
                'id': 'q1',
                'question': '1. What is the capital of France?',
                'locked': True,
                'options': [
                    {'id': 'a1', 'text': 'London'},
                    {'id': 'a2', 'text': 'Berlin'},
                    {'id': 'a3', 'text': 'Paris'},
                    {'id': 'a4', 'text': 'Rome'}
                ],
                'default': 2  # Default to 'Paris'
            },
            {
                'id': 'q2',
                'question': '2. What is 2 + 2?',
                'locked': False,
                'options': [
                    {'id': 'a5', 'text': '3'},
                    {'id': 'a6', 'text': '4'},
                    {'id': 'a7', 'text': '5'},
                    {'id': 'a8', 'text': '22'}
                ]
                # No default selection
            },
            {
                'id': 'q3',
                'question': '3. Which language is used for web apps?',
                'locked': True,
                'options': [
                    {'id': 'a9', 'text': 'Python'},
                    {'id': 'a10', 'text': 'Java'},
                    {'id': 'a11', 'text': 'C++'},
                    {'id': 'a12', 'text': 'All of the above'}
                ],
                'default': 3  # Default to 'All of the above'
            }
        ]
    }

    # Run the quiz and get the answers
    answers = main(quiz)
    # Print the answers
    for ans in answers:
        print(f"Question ID: {ans['question_id']}")
        print(f"Default Answer ID: {ans['default_answer_id']}")
        if ans['answer_id']:
            print(f"Selected Answer ID: {ans['answer_id']}\n")
        else:
            print("No Answer Selected\n")
