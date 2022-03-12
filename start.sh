
# check is there directory named dataset
# and check if there are files
DIRECTORY='dataset'
OUTDIR='output'
if [ ! -d $DIRECTORY ];then
    echo "ERROR: no such directory: $DIRECTORY"
    echo "Please check you work directory is right..."
    exit 1
else
    if [ "$(ls -A $DIRECTORY)" = "" ];then
        echo "ERROR: no files in directory: $DIRECTORY"
        echo "Please check there is file in the $DIRECTORY directory."
        exit 2
    fi
fi

echo "Find files..."

# get all file name
files=$(ls $DIRECTORY)

if [ ! -d $OUTDIR ];then
    # if there is no output directory, create a new one
    echo "No such directory: $OUTDIR."
    echo "Create directory: $OUTDIR..."
    mkdir $OUTDIR
fi

echo "Start transferring..."
for file in $files
do
    file_path=./$DIRECTORY/$file
    echo $file_path
    python3 transfer.py $file_path
done

echo "Run successfully!"
exit 0

