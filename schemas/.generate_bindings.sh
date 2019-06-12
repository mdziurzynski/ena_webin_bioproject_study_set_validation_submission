for filename in ENA.project SRA.experiment SRA.receipt SRA.run SRA.sample SRA.study SRA.submission
do
    urlbase="ftp://ftp.sra.ebi.ac.uk/meta/xsd/sra_1_5/"
    file="${urlbase}${filename}.xsd"
    outputFilename=${filename//\./_}
    
    echo $file
    pyxbgen -u $file -m $outputFilename || exit 1
    
    #fixing issues with module resolution
    sed -i -e 's/import _com as _ImportedBinding__com/from schemas import _com as _ImportedBinding__com/g' ${outputFilename}.py
done
