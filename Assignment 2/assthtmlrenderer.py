"""A program to display the output of the line_edits function in an
   html table.
   Written for COSC262 DP Assignment 
   Richard Lobb February 2020.
"""
import os
import re
from html import escape
import webbrowser
import sys

DEFAULT_CSS = """
table {font-size: 100%; border-collapse: collapse}
td, th  {border: 1px solid LightGrey; padding: 2px; }
td del {background-color: #FFBB00; text-decoration: none;}
"""

class HtmlTable:
    """A table to be rendered in HTML."""
    def __init__(self, column_headers):
        """The column headers is a list of strings. Its length determines the
           number of columns in the table"""
        self.headers = column_headers
        self.num_cols = len(column_headers)
        self._html = ""
        self._html += "<tr>" + ''.join(f"<th>{hdr}</th>" for hdr in column_headers) + "</tr>\n"

    def add_row(self, values, column_styles=None):
        """Given a list of strings ('values'), the length of which must match
           the length of the list of column headers when the table was created,
           add one row to the table. column_styles is an optional list of
           strings for setting the style attributes of the row's <td>
           elements. If given, its length must match the number of columns.

           For example
              add_row(["this", "that"], ["background-color:yellow", ""])

           would add a table row containing the values 'this' and 'that' with the
           first column having a background-color of yellow. An empty style
           string is ignored.
           String values are html-escaped (i.e. characters like '&' and '<' get
           converted to HTML-entities). Then, as a special feature for this
           assignment, any sequence of characters wrapped in double square
           brackets is instead wrapped in HTML <del> elements; these are by
           default rendered with a purple background by the HTML renderer.
           Then any newline characters are converted to <br>.
           Finally the resulting string is wrapped in a <pre> element.
        """
        def td_element(value, style, i_column):
            value = escape(value)  # HTML escaping
            value = re.sub(r'\[\[(..*?)\]\]', r'<del>\1</del>', value,
                flags=re.DOTALL + re.MULTILINE)
            value = value.replace('\n', '<br>')
            style_string = f' style="{style}"' if style else ''
            td = f"<td{style_string}><pre>{value}</pre></td>"
            return td

        if column_styles is None:
            column_styles = ["" for i in range(self.num_cols)]
        tds = [td_element(values[i], column_styles[i], i) for i in range(self.num_cols)]
        row = f"<tr>{''.join(tds)}</tr>\n"
        self._html += row

    def html(self):
        return "<table>\n" + self._html + "</table>\n"


class HtmlRenderer:
    """A class to help with displaying HTML for COSC262 Assignment 1, 2020.
       Once constructed"""
    def __init__(self, css=DEFAULT_CSS):
        """Initialise self to contain the given html string"""
        self.html = ''
        self.css = css

    def add_html(self, html):
        """Concatenate the given html to the end of the current html string"""
        self.html += html

    def render(self):
        """Display the current html in a browser window"""
        html = f"""<html><head><style>{self.css}</style></head><body>{self.html}</body></html>"""
        path = os.path.abspath('temp.html')
        with open(path, 'w') as f:
            f.write(html)
        webbrowser.open('file://' + path)


def edit_table(operations):
    """Construct an HtmlTable to display the given sequence of operations, as
       returned by the line_edits function.
    """
    table = HtmlTable(["Previous", "Current"])
    grey = "background-color:LightGrey"
    for op, left, right in operations:
        if op == 'C':
            table.add_row([left, right])
        elif op == 'D':
            table.add_row([left, right], ["background-color:#BBBBFF", grey])
        elif op == 'S':
            bg = "background-color:#FFFF99"
            table.add_row([left, right], [bg, bg])
        else:
            table.add_row([left, right], [grey, "background-color:#ABEBC6"])
    return table


#************************************************************************
#
# Your line_edits function and any support functions goes here.
from collections import deque

def lcs(s1, s2):
    """
    Find the longest common subsequence (LCS) between two strings
    Returns The longest common subsequence between s1 and s2.
    """
    # s1 (str): First string.
    m = len(s1)
    # s2 (str): Second string.
    n = len(s2)

    # Initialize a (m+1)x(n+1) matrix
    C = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill in the matrix with LCS lengths
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]: 
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])

    # Backtrack to find the sequence
    i, j = m, n
    lcs_str = ""

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str = s1[i - 1] + lcs_str
            i -= 1
            j -= 1
        elif C[i - 1][j] >= C[i][j - 1]:  # if the character from s1 is not part of LCS
            i -= 1
        else:  # if the character from s2 is not part of LCS
            j -= 1

    return lcs_str

def lcs_and_mark_extras(s1, s2):
    """
    Find the LCS between two strings and mark extra characters
    Returns A tuple with the LCS and extra characters marked in s1 and s2.
    """
    lcs_str = lcs(s1, s2)
    lcs_deque = deque(lcs_str)

    def mark_extras(s, lcs_deque):
        result = []

        for c in s:
            if lcs_deque and lcs_deque[0] == c:
                lcs_deque.popleft()
                result.append(c)
            else:
                result.append(f"[[{c}]]")  # mark extra characters

        return "".join(result)

    return mark_extras(s1, lcs_deque.copy()), mark_extras(s2, lcs_deque.copy())

def line_edits(s1, s2):
    """
    Find the line edit operations to transform one string into another.
    Returns A list of operations to transform s1 into s2.
    """
    lines1 = s1.splitlines()
    lines2 = s2.splitlines()

    # Source string
    n = len(lines1)
    # Target string
    m = len(lines2)

    # Initialize cost and operation matrices
    cost = [[0] * (m + 1) for _ in range(n + 1)]
    op = [[''] * (m + 1) for _ in range(n + 1)]

    # Fill in base cases
    for i in range(1, n + 1):
        cost[i][0] = i
        op[i][0] = 'D'  # Delete operation
    for j in range(1, m + 1):
        cost[0][j] = j
        op[0][j] = 'I'  # Insert operation

    # Fill in the rest of the matrices
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            delete_cost = cost[i - 1][j] + 1
            insert_cost = cost[i][j - 1] + 1

            if lines1[i - 1] == lines2[j - 1]:  # If lines are identical
                copy_cost = cost[i - 1][j - 1]
                min_cost = min(delete_cost, insert_cost, copy_cost)

                # Decide operation based on min_cost
                if min_cost == copy_cost:
                    op[i][j] = 'C'  # Copy operation
                elif min_cost == delete_cost:
                    op[i][j] = 'D'  # Delete operation
                else:
                    op[i][j] = 'I'  # Insert operation
            else:  # If lines are different
                substitute_cost = cost[i - 1][j - 1] + 1
                min_cost = min(delete_cost, insert_cost, substitute_cost)

                # Decide operation based on min_cost
                if min_cost == substitute_cost:
                    op[i][j] = 'S'  # Substitute operation
                elif min_cost == delete_cost:
                    op[i][j] = 'D'  # Delete operation
                else:
                    op[i][j] = 'I'  # Insert operation

            cost[i][j] = min_cost

    # Construct list of operations by backtracking
    operations = []
    i, j = n, m

    while i > 0 or j > 0:
        if op[i][j] == 'C':  # Copy
            operations.append(('C', lines1[i - 1], lines2[j - 1]))
            i -= 1
            j -= 1
        elif op[i][j] == 'S':  # Substitute
            left, right = lcs_and_mark_extras(lines1[i - 1], lines2[j - 1])
            operations.append(('S', left, right))
            i -= 1
            j -= 1
        elif op[i][j] == 'D':  # Delete
            operations.append(('D', lines1[i - 1], ''))
            i -= 1
        else:  # Insert
            operations.append(('I', '', lines2[j - 1]))
            j -= 1

    # Reverse the operations list to get the correct order
    operations.reverse()

    return operations
#
#************************************************************************


def main(s1, s2):
    renderer = HtmlRenderer()
    renderer.add_html("<h1>Show Differences (COSC262 2020)</h1>")
    operations = line_edits(s1, s2)
    table = edit_table(operations)
    renderer.add_html(table.html())
    renderer.render()

# Two example strings s1 and s2, follow.
# These are the same ones used in the assignment spec.

s1 = r'''# ============== DELETEs =====================
# TODO: add docstrings
@app.route('/queue/<hostname>', methods=['DELETE'])
def delete(hostname):
    try:
        data = json.loads(request.get_data())
        mac_address = data['macAddress']
    except:
        abort(400, 'Missing or invalid user data')
    status = queue.dequeue(hostname, macAddress)
    return ('', status)


@app.route('/queue', methods=['DELETE'])
def empty_queue():
    if request.remote_addr.upper() != TUTOR_MACHINE.upper():
        abort(403, "Not authorised")
    else:
        queue.clear_queue()
        response = jsonify({"message": "Queue emptied"})
        response.status_code = 204
        return response
'''

s2 = r'''# ============== DELETEs =====================
@app.route('/queue/<hostname>', methods=['DELETE'])
def delete(hostname):
    """Handle delete request from the given host"""
    try:
        data = json.loads(request.get_data())
        mac_address = data['mac_address']
    except:
        abort(400, 'Missing or invalid user data')
    status = queue.dequeue(hostname, mac_address)
    return ('', status)


@app.route('/queue', methods=['DELETE'])
def clear_queue():
    """Clear the queue. Valid only if coming from tutor machine"""
    if request.remote_addr.upper() != TUTOR_MACHINE.upper():
        abort(403, "Only the tutor machine can clear the queue")
    else:
        queue.clear_queue()
        response = jsonify({"message": "Queue cleared"})
        response.status_code = 204
        return response
'''

main(s1, s2)