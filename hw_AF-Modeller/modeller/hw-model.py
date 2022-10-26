import modeller
from modeller.automodel import AutoModel, allhmodel

modeller.log.verbose()
env = modeller.Environ()
env.io.atom_files_directory = ['.']
env.io.hydrogen = True


aln = modeller.Alignment(env)
aln.append(file='vh.fasta', alignment_format='FASTA', align_codes='VH')
template_model = modeller.Model(env, file='3bky_VH.pdb')
aln.append_model(template_model, align_codes='3bky_VH')
aln.align(gap_penalties_1d=(-600, -400))
aln.write(file="aln.ali")


a = allhmodel(env,
        alnfile  = "aln.ali",     # alignment filename
        knowns   = ('3bky_VH'),   # codes of the templates
        sequence = ('VH'))        # code of the target
a.starting_model = 1              # index of the first model
a.ending_model = 1                # index of the last model
                                  # (determines how many models to calculate)
a.make()                          # do comparative modeling
a.write("modeller_result.pdb")
