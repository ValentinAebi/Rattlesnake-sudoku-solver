# Script to run the compiler on all Rattlesnake files in src directory

from os import listdir, system
import sys

src_dir = "src"
rattlesnake_ext = ".rsn"
jar_file = "Rattlesnake.jar"

if __name__ == "__main__":
    compiler_cmd = sys.argv[1]
    sources = listdir(src_dir)
    rsn_sources = list(filter(lambda name: name.endswith(rattlesnake_ext), sources))
    for i in range(len(rsn_sources)):
        rsn_sources[i] = f"{src_dir}/{rsn_sources[i]}"
    cmd = f"java -jar {jar_file} {compiler_cmd} {' '.join(rsn_sources)}"
    system(cmd)
