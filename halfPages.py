from datetime import date, timedelta

_weekdayDict = {
        0 : "Monday",
        1 : "Tuesday",
        2 : "Wednesday",
        3 : "Thursday",
        4 : "Friday",
        5 : "Saturday",
        6 : "Sunday"
        }

_monthDict = {
        1 : "January",
        2 : "Februrary",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10: "October",
        11: "November",
        12: "December"
        }

# Page Functions
def _num_suffix(num):
    if num % 10 == 1:
        return "st"
    if num % 10 == 2:
        return "nd"
    if num % 10 == 3:
        return "rd"
    return "th"


def print_title(output, title, subtitle, ownerName, phoneNumber, address1, address2, city, state, country, zipCode):
    output.write("\\begin{tikzpicture}[\n"
        + "\tinner sep=3 pt,\n"
        + "\ttitle/.style={%\n"
        + "\t\tanchor = south,\n"
        + "\t\tnode font=\\Huge,\n"
        + "\t\talign=center,\n"
        + "\t},\n"
        + "\tsubtitle/.style={%\n"
        + "\t\tanchor = south,\n"
        + "\t\tnode font=\\huge,\n"
        + "\t\talign=center,\n"
        + "\t},\n"
        + "\tcontactinfo/.style={%\n"
        + "\t\tanchor = north west,\n"
        + "\t\tnode font=\\normalsize,\n"
        + "\t\talign=left,\n"
        + "\t},\n"
        + "\tyscale = -1]\n"
        + "\t% Framing Nodes\n"
        + "\t\\node at (0,0) {};\n"
        + "\t\\node at (11,17) {};\n"
        + "\n"
        + "\t% Title and Subtitle\n"
        + f"\t\\node at (5.5,7) [title] {{{title}}};\n"
        + f"\t\\node at (5.5, 8) [subtitle] {{{subtitle}}};\n"
        + "\n"
        + "\t% Contact Info\n"
        + "\t\\draw (2.75,11.5) rectangle (8.75,14);\n"
        + "\t\\foreach \\i in {11.5, 12, ..., 14}{\n"
        + "\t\t\\draw [thin, gray] (2.75, \\i) -- (8.75, \\i);\n"
        + "\t}\n"
        + "\n"
        + f"\t\\node at (2.75, 11.5) [contactinfo] {{{ownerName}}};\n"
        + f"\t\\node at (2.75, 12) [contactinfo] {{{phoneNumber}}};\n"
        + f"\t\\node at (2.75, 12.5) [contactinfo] {{{address1}}};\n"
        + f"\t\\node at (2.75, 13) [contactinfo] {{{address2}}};\n"
        + f"\t\\node at (2.75, 13.5) [contactinfo] {{{city}, {state} {zipCode} {country}}};\n"
        + "\n"
        + "\\end{tikzpicture}\n"
        + "\\begin{tikzpicture}[\n"
        + "\tinner sep=3 pt,\n"
        + "\ttitle/.style={%\n"
        + "\t\tnode font=\\Large,\n"
        + "\t},\n"
        + "\tyscale = -1]\n"
        + "\t% Framing Nodes\n"
        + "\t\\node at (0,0) {};\n"
        + "\t\\node at (11,17) {};\n"
        + "\\end{tikzpicture}\n"
        + "\\begin{tikzpicture}[\n"
        + "\tinner sep=3 pt,\n"
        + "\ttitle/.style={%\n"
        + "\t\tnode font=\\Large,\n"
        + "\t},\n"
        + "\tyscale = -1]\n"
        + "\t% Framing Nodes\n"
        + "\t\\node at (0,0) {};\n"
        + "\t\\node at (11,17) {};\n"
        + "\n"
        + "\\end{tikzpicture}\n")


def print_year(output, currDate):
    pass

def print_quarter(output, currDate):
    pass

def print_month(output, currDate):
    pass

def print_week(output, currDate):
    output.write("\\begin{tikzpicture}[\n"
            + "\tinner sep=3 pt,\n"
            + "\ttitle/.style={%\n"
            + "\t\tnode font=\\Large,\n"
            + "\t},\n"
            + "\tsubtitle/.style={%\n"
            + "\t\tanchor = west,\n"
            + "\t\tnode font=\\large,\n"
            + "\t},\n"
            + "\tday/.style={%\n"
            + "\t\tanchor = west,\n"
            + "\t\tnode font=\\normalsize,\n"
            + "\t},\n"
            + "\thabitdate/.style={%\n"
            + "\t\tanchor = north west,\n"
            + "\t\tnode font = \\footnotesize,\n"
            + "\t},\n"
            + "\thabit/.style={\n"
            + "\t\tanchor = north west,\n"
            + "\t\tnode font = \\footnotesize,\n"
            + "\t},\n"
            + "\tyscale = -1]\n"
            + "\t% Framing Nodes\n"
            + "\t\\node at (0,0) {};\n"
            + "\t\\node at (11,17) {};\n"
            + "\n"
            + "\t% ToDo list lines\n"
            + "\t\\foreach \\i in {1.5, 2, ..., 10.5}{\n"
            + "\t\t\\draw [gray, thin] (1, \\i) -- (5.25, \\i);\n"
            + "\t}\n"
            + "\t% Check Boxes\n"
            + "\t\\foreach \\i in {1, 1.5, ..., 10}{\n"
            + "\t\t\\draw (0.6,\\i+.1) rectangle (0.9,\\i+0.4);\n"
            + "\t}\n"
            + "\n"
            + "\t% Meal Plan Separator\n"
            + "\t\\draw [thick] (0.5, 10.5) -- (10.5, 10.5);\n"
            + "\n"
            + "\t% Meal Plan Day Lines\n"
            + "\t\\foreach \\i in {11.25, 12, ..., 16.5}{\n"
            + "\t\t\\draw (0.5, \\i) -- (5.5, \\i);\n"
            + "\t}\n"
            + "\t\\node [subtitle] at (1.9, 10.9) {Meal Plan};\n"
            + "\t\\node [day] at (0.5, 11.65) {M:};\n"
            + "\t\\node [day] at (0.5, 12.40) {T:};\n"
            + "\t\\node [day] at (0.5, 13.15) {W:};\n"
            + "\t\\node [day] at (0.5, 13.90) {R:};\n"
            + "\t\\node [day] at (0.5, 14.65) {F:};\n"
            + "\t\\node [day] at (0.5, 15.40) {S:};\n"
            + "\t\\node [day] at (0.5, 16.15) {S:};\n"
            + "\n"
            + "\t% Notes section\n"
            + "\t\\node [subtitle] at (7.4, 1.4) {Notes};\n"
            + "\t\\foreach \\i in {1.76, 2.14, ..., 10.5}{\n"
            + "\t\t\\draw [gray, thin] (5.5, \\i) -- (10.5, \\i);\n"
            + "\t}\n"
            + "\n"
            + "\t% Habits Section\n"
            + "\t% Vertical\n"
            + "\t\\foreach \\i in {7.5, 7.875, ..., 10.5}{\n"
            + "\t\t\\draw  [gray, thin] (\\i, 10.5) -- (\\i, 16.5);\n"
            + "\t}\n"
            + "\t\\draw (7.5, 10.5) -- (7.5, 16.5);\n"
            + "\n"
            + "\t% Horizontal\n"
            + "\t\\foreach \\i in {11, 11.5, ..., 16.5}{\n"
            + "\t\t\\draw (5.5, \\i) -- (10.5, \\i);\n"
            + "\t}\n"
            + "\t\\draw [thick] (5.5, 11) -- (10.5,11);\n"
            + "\n"
            + "\t% Text\n"
            + "\t\\node [anchor=north west] at (5.5, 10.52) {Habit};\n"
            + "\t\\node [habitdate] at (7.43, 10.55) {M};\n"
            + "\t\\node [habitdate] at (7.835, 10.55) {T};\n"
            + "\t\\node [habitdate] at (8.16, 10.55) {W};\n"
            + "\t\\node [habitdate] at (8.58, 10.55) {R};\n"
            + "\t\\node [habitdate] at (8.975, 10.55) {F};\n"
            + "\t\\node [habitdate] at (9.36, 10.55) {S};\n"
            + "\t\\node [habitdate] at (9.74, 10.55) {S};\n"
            + "\t\\node [habitdate] at (10.07, 10.52) {\\#};\n"
            + "\n"
            + "\t\\node [habit] at (5.5, 11.05) {Exercise};\n"
            + "\t\\node [habit] at (5.5, 11.55) {Sleep 11-8};\n"
            + "\t\\node [habit] at (5.5, 12.05) {Pets};\n"
            + "\t\\node [habit] at (5.5, 12.55) {Read};\n"
            + "\t\\node [habit] at (5.5, 13.05) {Meditate};\n"
            + "\t\\node [habit] at (5.5, 13.55) {Vit./Meds.};\n"
            + "\t\\node [habit] at (5.5, 14.05) {Eat Healthy};\n"
            + "\n"
            + "\t\\node [habit] at (10.125, 11.05) {5};\n"
            + "\t\\node [habit] at (10.125, 11.55) {7};\n"
            + "\t\\node [habit] at (10.125, 12.05) {7};\n"
            + "\t\\node [habit] at (10.125, 12.55) {7};\n"
            + "\t\\node [habit] at (10.125, 13.05) {7};\n"
            + "\t\\node [habit] at (10.125, 13.55) {7};\n"
            + "\t\\node [habit] at (10.125, 14.05) {6};\n"
            + "\n"
            + "\t% Vertical Split\n"
            + "\t\\draw [thick] (5.5,1) -- (5.5, 16.5);\n"
            + "\n"
            + "\t% Date / Title and Border Lines\n"
            + f"\t\\node at (0.5,0.4) [title] [anchor=north west] {{ Week of {_monthDict[currDate.month]} {currDate.day}{_num_suffix(currDate.day)}"
                + f" - {_monthDict[(currDate + timedelta(days=6)).month]+' ' if (currDate + timedelta(days=6)).month != currDate.month else ''}"
                + f"{(currDate + timedelta(days=6)).day}{_num_suffix((currDate + timedelta(days=6)).day)}, {(currDate + timedelta(days=6)).year}}};\n"
            + "\t\\draw [thick] (0.5,1) -- (10.5,1);\n"
            + "\t\\draw [thick] (0.5, 16.5) -- (10.5, 16.5);\n"
            + "\t\\draw [thick] (0.5, 1) -- (0.5, 16.5);\n"
            + "\t\\draw [thick] (10.5, 1) -- (10.5, 16.5);\n"
            + "\n"
            + "\\end{tikzpicture}\n"
            + "\\begin{tikzpicture}[\n"
            + "\tinner sep=3 pt,\n"
            + "\ttitle/.style={%\n"
            + "\t\tnode font=\\Large,\n"
            + "\t},\n"
            + "\tday/.style={%\n"
            + "\t\tanchor=west,\n"
            + "\t\tnode font=\\small,\n"
            + "\t},\n"
            + "\tdate/.style={%\n"
            + "\t\tanchor = east,\n"
            + "\t\tnode font=\\scriptsize,\n"
            + "\t\tcolor=gray,\n"
            + "\t},\n"
            + "\tyscale = -1]\n"
            + "\t% Framing Nodes\n"
            + "\t\\node at (0,0) {};\n"
            + "\t\\node at (11,17) {};\n"
            + "\n"
            + "\t% Minor Horizontal Lines\n"
            + "\t\\foreach \\i in {1.5, 2, ..., 16}{\n"
            + "\t\t\\draw [gray, thin] (0.75, \\i) -- (3.58333, \\i);\n"
            + "\t\t\\draw [gray, thin] (4.08333, \\i) -- (6.91666, \\i);\n"
            + "\t\t\\draw [gray, thin] (7.41666, \\i) -- (10.25, \\i);\n"
            + "\n"
            + "\t}\n"
            + "\n"
            + "\n"
            + "\t% Date / Title and Border Lines\n"
            + "\t\\node at (0.5,0.4) [title] [anchor=north west] {Events, Appointments, and Due Dates};\n"
            + "\t\\draw [thick] (0.5,1) -- (10.5,1);\n"
            + "\t\\draw [thick] (0.5, 16.5) -- (10.5, 16.5);\n"
            + "\t\\draw [thick] (0.5, 1) -- (0.5, 16.5);\n"
            + "\t\\draw [thick] (10.5, 1) -- (10.5, 16.5);\n"
            + "\t\\draw [thick] (0.5, 8.5) -- (10.5, 8.5);\n"
            + "\t\\draw [thick] (7.16666, 12.5) -- (10.5, 12.5);\n"
            + "\n"
            + "\t% Major Horizontal Lines\n"
            + "\t\\draw (0.5, 1.5) -- (10.5, 1.5);\n"
            + "\t\\draw (0.5, 9) -- (10.5, 9);\n"
            + "\t\\draw (7.16666, 13) -- (10.5, 13);\n"
            + "\n"
            + "\t% Days / Dates\n"
            + "\t\\node [day] at (0.5, 1.28) {Monday};\n"
            + "\t\\node [day] at (3.83333, 1.28) {Tuesday};\n"
            + "\t\\node [day] at (7.16666, 1.28) {Wednesday};\n"
            + "\t\\node [day] at (0.5, 8.78) {Thursday};\n"
            + "\t\\node [day] at (3.83333, 8.78) {Friday};\n"
            + "\t\\node [day] at (7.16666, 8.78) {Saturday};\n"
            + "\t\\node [day] at (7.16666, 12.78) {Sunday};\n"
            + "\n"
            + f"\t\\node [date] at (3.83333, 1.28) {{{currDate.strftime('%m/%d')}}};\n"
            + f"\t\\node [date] at (7.16666, 1.28) {{{(currDate + timedelta(days=1)).strftime('%m/%d')}}};\n"
            + f"\t\\node [date] at (10.5, 1.28) {{{(currDate + timedelta(days=2)).strftime('%m/%d')}}};\n"
            + f"\t\\node [date] at (3.83333, 8.78) {{{(currDate + timedelta(days=3)).strftime('%m/%d')}}};\n"
            + f"\t\\node [date] at (7.16666, 8.78) {{{(currDate + timedelta(days=4)).strftime('%m/%d')}}};\n"
            + f"\t\\node [date] at (10.5, 8.78) {{{(currDate + timedelta(days=5)).strftime('%m/%d')}}};\n"
            + f"\t\\node [date] at (10.5, 12.78) {{{(currDate + timedelta(days=6)).strftime('%m/%d')}}};\n"
            + "\n"
            + "\t% Vertical Lines\n"
            + "\t\\foreach \\i in {0.5, 3.83333, ..., 10.5}{\n"
            + "\t\t\\draw [thick] (\\i, 1) -- (\\i, 16.5);\n"
            + "\t}\n"
            + "\\end{tikzpicture}\n")

def print_day(output, currDate):
    output.write("\\begin{tikzpicture}[\n"
            + "\tinner sep=3 pt,\n"
            + "\ttitle/.style={%\n"
            + "\t\tnode font=\\Large,\n"
            + "\t},\n"
            + "\thournumber/.style={%\n"
            + "\t\tanchor = west,\n"
            + "\t\tnode font=\\small,\n"
            + "\t},\n"
            + "\tminutenumber/.style={%\n"
            + "\t\tanchor = west,\n"
            + "\t\tnode font=\\tiny,\n"
            + "\t\tcolor=gray,\n"
            + "\t},\n"
            + "\tyscale = -1]\n"
            + "\t% Framing Nodes\n"
            + "\t\\node at (0,0) {};\n"
            + "\t\\node at (11,17) {};\n"
            + "\t\n"
            + "\t% Date / Title and Border Lines\n"
            + f"\t\\node at (0.5,0.4) [title] [anchor=north west] {{{_weekdayDict[currDate.weekday()]}, {_monthDict[currDate.month]} {currDate.day}{_num_suffix(currDate.day)} {currDate.year}}};\n"
            + "\t\\draw [thick] (0.5,1) -- (10.5,1);\n"
            + "\t\\draw [thick] (0.5, 16.5) -- (10.5, 16.5);\n"
            + "\t\\draw [thick] (0.5, 1) -- (0.5, 16.5);\n"
            + "\t\\draw [thick] (10.5, 1) -- (10.5, 16.5);\n"
            + "\n"
            + "\t% Hour Numbers\n"
            + "\t\\foreach \\i in {0, 1, ..., 11}{\n"
            + "\t\t\\node [hournumber] at (0.5, \\i*15.5/12 + 1.3) {\\i};\n"
            + "\t}\n"
            + "\t\n"
            + "\t% Minute Numbers\n"
            + "\t\\foreach \\i in {0, 1, ..., 11}{\n"
            + "\t\t\\node [minutenumber] at (0.5, \\i*15.5/12 + 2) {:30};\n"
            + "\t}\n"
            + "\n"
            + "\t% Vertical Lines\n"
            + "\t\\draw (1,1) -- (1, 16.5);\n"
            + "\t\\foreach \\i in {1, 4.16673, ..., 10.5}{\n"
            + "\t\t\\draw (\\i, 1) -- (\\i, 16.5);\n"
            + "\t}\n"
            + "\n"
            + "\t% Minor Horizontal Lines\n"
            + "\t\\foreach \\i in {0.5, 1.5, ..., 11.5}{\n"
            + "\t\t\\draw [gray, thin] (1, \\i*15.5/12 + 1) -- (10.5, \\i*15.5/12 + 1);\n"
            + "\t}\n"
            + "\n"
            + "\t% Major Horizontal Lines\n"
            + "\t\\foreach \\i in {0, 1, ..., 11}{\n"
            + "\t\t\\draw (0.5, \\i*15.5/12 + 1) -- (10.5, \\i*15.5/12 + 1);\n"
            + "\t}\n"
            + "\t\n"
            + "\\end{tikzpicture}\n"
            + "\t\\begin{tikzpicture}[\n"
            + "\tinner sep=3 pt,\n"
            + "\ttitle/.style={%\n"
            + "\t\tnode font=\\Large,\n"
            + "\t},\n"
            + "\thournumber/.style={%\n"
            + "\t\tanchor=west,\n"
            + "\t\tnode font=\\small, \n"
            + "\t},\n"
            + "\tminutenumber/.style={%\n"
            + "\t\tanchor = west,\n"
            + "\t\tnode font=\\tiny, \n"
            + "\t\tcolor=gray,\n"
            + "\t},\n"
            + "\tyscale = -1]\n"
            + "\t% Framing Nodes\n"
            + "\t\\node at (0,0) {};\n"
            + "\t\\node at (11,17) {};\n"
            + "\t\n"
            + "\t% Date / Title and Border Lines\n"
            + "\t\\draw [thick] (0.5,1) -- (10.5,1);\n"
            + "\t\\draw [thick] (0.5, 16.5) -- (10.5, 16.5);\n"
            + "\t\\draw [thick] (0.5, 1) -- (0.5, 16.5);\n"
            + "\t\\draw [thick] (10.5, 1) -- (10.5, 16.5);\n"
            + "\n"
            + "\t% Hour Numbers\n"
            + "\t\\foreach \\i [evaluate=\\i as \\n using int(\\i+12)] in {0, 1, ..., 11}{\n"
            + "\t\t\\node [hournumber] at (0.5, \\i*15.5/12 + 1.3) {\\n};\n"
            + "\t}\n"
            + "\t\n"
            + "% Minute Numbers\n"
            + "\t\\foreach \\i in {0, 1, ..., 11}{\n"
            + "\t\t\\node [minutenumber] at (0.5, \\i*15.5/12 + 2) {:30};\n"
            + "\t}\n"
            + "\n"
            + "\t% Vertical Lines\n"
            + "\t\\draw (1,1) -- (1, 16.5);\n"
            + "\t\\foreach \\i in {1, 4.16673, ..., 10.5}{\n"
            + "\t\t\\draw (\\i, 1) -- (\\i, 16.5);\n"
            + "\t}\n"
            + "\n"
            + "\t% Minor Horizontal Lines\n"
            + "\t\\foreach \\i in {0.5, 1.5, ..., 11.5}{\n"
            + "\t\t\\draw [gray, thin] (1, \\i*15.5/12 + 1) -- (10.5, \\i*15.5/12 + 1);\n"
            + "\t}\n"
            + "\n"
            + "\t% Major Horizontal Lines\n"
            + "\t\\foreach \\i in {0, 1, ..., 11}{\n"
            + "\t\t\\draw (0.5, \\i*15.5/12 + 1) -- (10.5, \\i*15.5/12 + 1);\n"
            + "\t}\n"
            + "\t\n"
            + "\\end{tikzpicture}\n")
