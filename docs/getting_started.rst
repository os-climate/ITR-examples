**************************
Getting Started with the ITR Tools
**************************


The OS-Climate project has developed both a stand-alone GUI tool as well as a some sample Jupyter Notebooks that make it possible to evaluate and explore the GFANZ ITR methodology as it applies to company, portfolio, and sector alignment with Net-Zero goals.  No coding is required to use these tools, but some coding knowledge is very helpful to get the most out of the Jupyter Notebooks (or to make your own changes to the GUI tool).

The first step is to create an environment that allows you to run Python (minimum version Python 3.9) and install and activate a virtual environment.  You can follow these instructions from the Python documentation: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/  You only need to follow up to the :code:`Installing packages` part.  Here is an example of the four commands needed to bring up the :code:`itr-ui` tool on Mac OSX by creating a virtual environment in the user's home directory :code:`virtualenvs`::

    python3 -m venv ~/virtualenvs/itr-examples
    . ~/virtualenvs/itr-examples/bin/activate
    pip install ITR-examples
    itr-ui

Note that the :code:`itr-ui` tool runs with provided sample data by default.  You can run the tool on your own data by providing a path to the sample data you have prepared, e.g., :code:`itr-ui my-data-directory/My-Sample-Data.xlsx`

**Getting Started with Git**

You will use :code:`git` to access the ITR source code.  You can install git in your virtual environment thusly: :code:`pip install git`.  But you can also get it other ways: https://github.com/git-guides/install-git

**Installing the ITR-examples environment and running the Notebook**

With your virtual environment running, and starting from the directory in which you want to do the testing:

1. Clone the ITR-examples repository: :code:`git clone https://github.com/os-climate/ITR-examples.git`
2. Change your directory to the top-level ITR-examples directory: :code:`cd ITR-examples`
3. Start your notebook: :code:`jupyter lab`.  This should cause your default browser to pop to the front and open a page with a Jupyter Notebook.
4. In the file browser on the left hand side of the Jupyter window, double-click on :code:`notebooks`.  You should see a file named :code:`quick_template_score_calc.ipynb`.  Double click on that file to open it.
5. Run the notebook with a fresh kernel by pressing the :code:`>>` button.  Accept the option to Restart Kernel and clear all previous variables.

The brackets listed near the top left corner of each executable cell will change from :code:`[ ]` (before running the notebook) to :code:`[*]` while the cell's computation is pending, to a number (such as :code:`[5]` for the 5th cell) when computation is complete.  If everything is working, you will see text output, graphical output, and a newly created `data_dump.xlsx` file representing the input porfolio, enhanced with temperature score data.

The ITR-examples environment contains other sample data sets in :code:`ITR-examples/src/ITR_examples/data`.

**Loading your own data**

By default, the :code:`quick_template_score_calc.ipynb` notebook uses data from the sample data template :code:`../src/ITR_examples/data/20220927 ITR V2 Sample Data.xlsx`.  You can change that:

1. Place your portfolio data file in the :code:`ITR-examples/src/ITR_examples/data` subdirectory.
2. If not already running, start the Jupyter environment: :code:`jupyter lab`
3. Open the notebook :code:`quick_template_score_calc.ipynb`
4. Scroll down to the section 'Download/load the sample template data'
5. Change the filename of the .xlsx in the line: :code:`for filename in ['data/<your_filename.xlsx>',`
6. Change the filename of the .xlsx in the line: :code:`template_data_path = "data/<your_filename.xlsx>"`
7. Run the notebook with a fresh kernel by pressing the :code:`>>` button.  Accept the option to Restart Kernel and clear all previous variables.


Filing Issues and Updating the ITR Repository
---------------------------------------------

Once you are able to run the `quick_template_score_calc.ipynb` sample notebook with the provided sample data (:code:`ITR-examples/src/ITR_examples/data/20230106 ITR Tool Sample Data.xlsx`), you are ready to start trying things with your own data.  The notebook explains how to do this at the heading labeled :code:`Download/load the sample template data` before Cell 6.  As you try loading your own data, you will inevitably find errors--sometimes with the data you receive, sometimes with the data you present to the tool, sometimes with the way the tool loads or does not load your data, sometimes with the way the tool interprets or presents your data.  It is the goal of the Data Commons to streamline and simplify access to data so as to reduce the first to cases of errors, and it is the goal of the ITR project team to continuously improve the ITR tool to reduce the other cases of errors.  In all cases, the correction of errors begins with an error reporting process and ends with an effective update process.

To report errors, please use the GitHub Issues interface for the ITR tool: https://github.com/os-climate/ITR-examples/issues

Immediately you will see all open issues filed against the tool, and you may find that a problem you are having has already been reported.  You can search for keywords, and usually in the process of solving issues, commentary on a specific issue may provide insights into work-arounds.  If you do not see an existing issue (you don't need to search exhaustively; just enough to save yourself time writing up an issue that's already been filed), then by all means open an issue describing the problem, ideally with a reproducible test case (such as an excel file containing the minimum amount of anonymozed data required to reproduce the problem).  The team can then assign the problem and you will see progress as the issue is worked.

The collective actions of many people reporting issues and many people working collaboratively to resolve issues is one of the great advantages of open source software development, and a great opportunity to see its magic at work.

At some point you will receive notice that your issue has been addressed with a new release.  If you are comfortable with :code:`git` you can update your repository with a :code:`git pull`, install new software with :code:`pip install -e .` and have at it.  This is the preferred route for people making contributions and staying in sync with developers.  But you can also simply :code:`pip install -U ITR-examples` and that will install the latest version of the tool.  It will not, however, update source-level data (such as alternative sample data).  It will only update the default installed sample data.  This is not a problem if you are only using your own data to drive the tool.
