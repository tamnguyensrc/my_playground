import aura.pipeline.library.*
import java.text.SimpleDateFormat

ci 'ecs-global-slave', {

    env.group = "aura"
    env.team = "playground"
    env.subteam = "playground"
    env.service_name = "my_playground"
    env.language = "python"
    env.service_git_repo = env.service_name
    env.service_git_project = "AURA"
    String version_type_patch = "patch", version_type_minor = "minor", version_type_major = "major"


    SimpleDateFormat formatter= new SimpleDateFormat("ddMM");
    Date date = new Date(System.currentTimeMillis());
    String today = formatter.format(date);
    echo "today: $today"

    checkout scm

    feature {
        auraPython.createBuildDistribution()
        auraPython.pip3InstallPackages()
    }

    pullrequest {
        auraGit.checkoutBranch(env.source_branch)
        auraPython.pip3InstallPackages()
        auraPython.uploadPackageToArtifactory("local", true)
    }

    develop {
        auraGit.checkoutBranch("develop")
        auraPython.pip3InstallPackages()
        auraPython.bumpPackageVersion(version_type_patch)
        auraPython.uploadPackageToArtifactory("local")
    }

    production {
        auraGit.checkoutBranch("master")
        auraPython.pip3InstallPackages()
        auraPython.bumpPackageVersion(version_type_minor)
        auraPython.uploadPackageToArtifactory("release")
    }
}
