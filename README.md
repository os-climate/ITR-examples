<!-- markdownlint-disable -->
<!-- prettier-ignore-start -->
> [!IMPORTANT]
> On June 26 2024, Linux Foundation announced the merger of its financial services umbrella, the Fintech Open Source Foundation ([FINOS](https://finos.org)), with OS-Climate, an open source community dedicated to building data technologies, modeling, and analytic tools that will drive global capital flows into climate change mitigation and resilience; OS-Climate projects are in the process of transitioning to the [FINOS governance framework](https://community.finos.org/docs/governance); read more on [finos.org/press/finos-join-forces-os-open-source-climate-sustainability-esg](https://finos.org/press/finos-join-forces-os-open-source-climate-sustainability-esg)
<!-- prettier-ignore-end -->
<!-- markdownlint-enable -->

# ITR-examples

Example data and user interface for the [ITR project](https://github.com/os-climate/ITR/)

## Getting started with the user interface

If you use Anaconda environments, open an Anaconda prompt window, navigate to the root of the ITR release (ITR-develop) and run:

    conda env create -f environment.yml
    conda activate itr_ui

For virtual environments, open a command prompt/terminal window, navigate to the root of the ITR release and run

    python3 -m venv itr_ui

On Unix or MacOS, activate the environment with

    source itr_ui/bin/activate

On Windows, activate the environment with

    itr_ui\Scripts\activate

To install the tool (or upgrade to the latest release) run:

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade itr-examples

Now you are ready to run the tool:

    itr-ui

You can also load specific content using the syntax:

    itr-ui "data/20230106 ITR V2 Sample Data.xlsx"

Note the python commands are `python` for windows and `python3` for linux/mac. If no file is specified, the tool uses a default, small ITR dataset. With a filename given, the ITR tool will load data from that dataset. The 20230106 data template has over 120 companies across nearly a dozen sectors.

Finally, to access the user interface open a browser window and navigate to: [http://127.0.0.1:8050/](http://127.0.0.1:8050/)

## Jupyter notebooks

To work with notebooks from the 'examples' directory please register the kernel from your virtual environment
such that it is available in Jupyter. Kernels from Anaconda environments will be available by default. Replace
`<env_name>` in the following command by your environment name (`itr_ui` or `itr_env`) and run it in your environment.

    python -m ipykernel install --user --name=<env_name>

Start Jupyter by activating your environment and running

    jupyter-notebook

## Getting started for Contributors/Developers

If you haven't done so already, follow the installation instructions above.

Make sure you have sourced the virtual environment using:

    source itr_env/bin/activate

...Or under Windows:

    itr_env\Scripts\activate

The commands below will upgrade to the latest release and install the components necessary for development:

    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade itr-examples
    pip install -e .[dev]

![docs/ITR_demo.gif](https://github.com/os-climate/ITR-examples/blob/main/docs/ITR_demo.gif)
