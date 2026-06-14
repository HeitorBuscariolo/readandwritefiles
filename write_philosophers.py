def main():
    #open a file named philosophers.txt
    outfile = open('philosophers.txt', 'w')

    #write the names of three philosophers to the file
    #John Locke, David Hume and Edmund Burke
    outfile.write('John Locke'+ '\n')
    outfile.write('David Hume'+ '\n')
    outfile.write('Edmund Burke'+ '\n')

    #close the file
    outfile.close()

#call the main function
main()