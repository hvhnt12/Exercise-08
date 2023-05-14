# TASK1
import os


def write_to_file(text, output_file_path):
    if os.path.exists(output_file_path):
        raise RuntimeError("Output file already exists!")
    with open(output_file_path, "w") as f:
        f.write(text)

# TASK2
import spacy


def count_stopwords(input_file_path):
    nlp = spacy.load("en_core_web_sm")
    with open(input_file_path, "r") as f:
        text = f.read()
    doc = nlp(text)
    stopword_count = sum(token.is_stop for token in doc)
    return stopword_count


# TASK3
import spacy


def remove_stopwords(input_file_path: str, output_file_path: str) -> None:
    nlp = spacy.load("en_core_web_sm")
    with open(input_file_path, "r") as input_file:
        text = input_file.read()
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    with open(output_file_path, "w") as output_file:
        output_file.write(" ".join(tokens))


# TASK4
import spacy


def tokenize_text(input_file_path, output_file_path):
    try:
        nlp = spacy.load("en_core_web_sm")

        with open(input_file_path, "r", encoding="utf-8") as input_file:
            text = input_file.read()

        doc = nlp(text)

        with open(output_file_path, "w", encoding="utf-8") as output_file:
            for token in doc:
                output_file.write(f"{token.text}\t{token.pos_}\t{token.dep_}\n")

    except FileNotFoundError:
        print(f"Error: input file '{input_file_path}' not found.")
    except PermissionError:
        print(f"Error: permission denied while trying to access file '{input_file_path}' or '{output_file_path}'.")


# TASK5
import spacy
from spacy import displacy


def save_visualization(input_file_path, output_file_path):
    nlp = spacy.load("en_core_web_sm")
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    doc = nlp(text)

    svg = displacy.render(doc, style="dep", options={"compact": True, "distance": 100})

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(svg)
