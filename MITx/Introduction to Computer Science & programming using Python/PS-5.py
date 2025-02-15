########################################################################################
## PROBLEM 1 ##

# The Message class contains methods that could be used to apply a cipher to a string,
# either to encrypt or to decrypt a message (since for Caesar codes this is the same action).
# In the next two questions, you will fill in the methods of the Message class found in ps6.py according to the specifications in the docstrings.
# The methods in the Message class already filled in are:
#
# __init__(self, text)
# The getter method get_message_text(self)
# The getter method get_valid_words(self), notice that this one returns a copy of self.valid_words to prevent someone from mutating the original list.
# In this problem, you will fill in two methods:
#
# Fill in the build_shift_dict(self, shift) method of the Message class. Be sure that your dictionary includes both lower and upper case letters,
# but that the shifted character for a lower case letter and its uppercase version are lower and upper case instances of the same letter.
# What this means is that if the original letter is "a" and its shifted value is "c", the letter "A" should shift to the letter "C".
# If you are unfamiliar with the ordering or characters of the English alphabet, we will be following
# the letter ordering displayed by string.ascii_lowercase and string.ascii_uppercase:
#
# >>> import string
# >>> print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
# >>> print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# A reminder from the introduction page - characters such as the space character, commas, periods,
# exclamation points, etc will not be encrypted by this cipher - basically, all the characters within string.punctuation,
# plus the space (' ') and all numerical characters (0 - 9) found in string.digits.
# Fill in the apply_shift(self, shift) method of the Message class. You may find it easier to use build_shift_dict(self, shift).
# Remember that spaces and punctuation should not be changed by the cipher.

##### Code snippet

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text
        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26
        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        lower_keys = list(string.ascii_lowercase)
        lower_values = list(string.ascii_lowercase)
        shift_lower_values = lower_values[shift:] + lower_values[:shift]

        upper_keys = list(string.ascii_uppercase)
        upper_values = list(string.ascii_uppercase)
        upper_shift_values = upper_values[shift:] + upper_values[:shift]

        full_keys = lower_keys + upper_keys
        full_values = shift_lower_values + upper_shift_values

        self.shift_dict = dict(zip(full_keys, full_values))
        return self.shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        new_msg = []
        for i in self.message_text:
            if i not in self.build_shift_dict(shift).keys():
                new_msg.append(i)
                continue
            else:
                new_msg.append(self.build_shift_dict(shift)[i])
        return ''.join(new_msg)

## Correct



########################################################################################
## PROBLEM 2 ##

# For this problem, the graders will use our implementation of the Message class, so don't worry if you did not get the previous parts correct.
#
# PlaintextMessage is a subclass of Message and has methods to encode a string using a specified shift value.
# Our class will always create an encoded version of the message, and will have methods for changing the encoding.
#
# Implement the methods in the class PlaintextMessage according to the specifications in ps6.py. The methods you should fill in are:
#
# __init__(self, text, shift): Use the parent class constructor to make your code more concise.
# The getter method get_shift(self)
# The getter method get_encrypting_dict(self): This should return a COPY of self.encrypting_dict to prevent someone from mutating the original dictionary.
# The getter method get_message_text_encrypted(self)
# change_shift(self, shift): Think about what other methods you can use to make this easier. It shouldn’t take more than a couple lines of code.

##### Code snippet

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message
        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        Hint: consider using the parent class constructor so less
        code is repeated
        '''
        # pass #delete this line and replace with your code here
        self.shift = shift
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        # pass #delete this line and replace with your code here
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class

        Returns: a COPY of self.encrypting_dict
        '''
        # pass #delete this line and replace with your code here
        encrypting_dict_copy = self.encrypting_dict.copy()
        return encrypting_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        # pass #delete this line and replace with your code here
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift (ie. self.encrypting_dict and
        message_text_encrypted).

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        Returns: nothing
        '''
        # pass #delete this line and replace with your code here
        self.shift = shift
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)

## Correct



########################################################################################
## PROBLEM 3 ##

# For this problem, the graders will use our implementation of the Message and PlaintextMessage classes, so don't worry if you did not get the previous parts correct.
# Given an encrypted message, if you know the shift used to encode the message, decoding it is trivial.
# If message is the encrypted message, and s is the shift used to encrypt the message, then apply_shift(message, 26-s) gives you the original plaintext message.
# Do you see why?
#  The problem, of course, is that you don’t know the shift. But our encryption method only has 26 distinct possible values for the shift!
#  We know English is the main language of these emails, so if we can write a program that tries each shift and maximizes
#  the number of English words in the decoded message, we can decrypt their cipher!
#  A simple indication of whether or not the correct shift has been found is if most of the words obtained after a shift are valid words.
#  Note that this only means that most of the words obtained are actual words.
#  It is possible to have a message that can be decoded by two separate shifts into different sets of words.
#  While there are various strategies for deciding between ambiguous decryptions, for this problem we are only looking for a simple solution.
#
# Fill in the methods in the class CiphertextMessage acording to the specifications in ps6.py. The methods you should fill in are:
#
# __init__(self, text): Use the parent class constructor to make your code more concise.
# decrypt_message(self): You may find the helper function is_word(wordlist, word) and the string method split() useful.
# Note that is_word will ignore punctuation and other special characters when considering whether a word is valid.

##### Code snippet

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.
        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return
        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        word_counter = 0
        max_count = 0
        for i in range(26):
            for j in list(super(CiphertextMessage, self).apply_shift(i).split(' ')):
                if is_word(self.valid_words, j):
                    word_counter += 1
                if word_counter > max_count:
                    max_count = word_counter
                    shift_value = i
                    decrypted_msg = super(CiphertextMessage, self).apply_shift(i)

        return (shift_value, decrypted_msg)

## Correct



########################################################################################
## PROBLEM 4 ##

# For this problem, the graders will use our implementation of the Message, PlaintextMessage, and CiphertextMessage classes,
# so don't worry if you did not get the previous parts correct.
# Now that you have all the pieces to the puzzle, please use them to decode the file story.txt.
# The file ps6.py contains a helper function get_story_string() that returns the encrypted version of the story as a string.
# Create a CiphertextMessage object using the story string and use decrypt_message to return the appropriate shift value and unencrypted story string.

##### Code snippet

def decrypt_story():
    joke_code = CiphertextMessage(get_story_string())
    return joke_code.decrypt_message()

## Correct