import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    result = {}
    N = len(corpus)
    const = (1 - damping_factor) / N

    # For pages linked to by the current page
    array = list(corpus[page])
    l = len(array)
    for p in array:
        result[p] = const + damping_factor / l

    # For pages not linked to by the current page
    for p in corpus:
        if p not in array:
            result[p] = const

    return result


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    results = {}
    count = n

    # Randomly choose first sample
    current = random.choice(list(corpus))
    results[current] = 1
    count -= 1

    # Process for choosing the rest of the samples
    while count > 0:
        # Pick next sample according to transition model
        options = transition_model(corpus, current, damping_factor)
        current = random.choices(list(options), weights = options.values())[0]

        # Update results dict
        if current in results:
            results[current] += 1
        else:
            results[current] = 1
        count -= 1

    for page in results:
        results[page] = results[page] / n

    return results


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    results = {}
    N = len(corpus)
    for page in corpus:
        results[page] = 1 / N

    # Iterative algorithm
    loop = True
    while loop:
        loop = False
        for p in results:
            results[p] = (1 - damping_factor) / N
            for q in corpus:
                array = corpus[q]
                if len(array) == 0:
                    results[p] += damping_factor * results[q] / N
                elif p in array:
                    diff = damping_factor * results[q] / len(array)
                    results[p] += diff
                    # Ensure all changes are 0.001 or less before breaking from loop
                    if diff > 0.001:
                        loop = True
    return results


if __name__ == "__main__":
    main()
