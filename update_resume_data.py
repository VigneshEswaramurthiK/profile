import re

def update_resume():
    with open('resume.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_content = """
                        <!-- Experience Section-->
                        <section>
                            <div class="d-flex align-items-center justify-content-between mb-4">
                                <h2 class="text-primary fw-bolder mb-0">Experience</h2>
                                <a class="btn btn-primary px-4 py-3" href="assets/Vignesh_Resume.pdf">
                                    <div class="d-inline-block bi bi-download me-2"></div>
                                    Download Resume
                                </a>
                            </div>
                            
                            <!-- Experience Card 1-->
                            <div class="card shadow border-0 rounded-4 mb-5">
                                <div class="card-body p-5">
                                    <div class="row align-items-center gx-5">
                                        <div class="col text-center text-lg-start mb-4 mb-lg-0">
                                            <div class="bg-transparent p-4 rounded-4">
                                                <div class="text-primary fw-bolder mb-2">April 2025 - Present</div>
                                                <div class="small fw-bolder">Lead Quality Engineer / AI Orchestrator</div>
                                                <div class="small text-light">iSON Xperiences</div>
                                                <div class="small text-light">Chennai, India</div>
                                            </div>
                                        </div>
                                        <div class="col-lg-8">
                                            <div>
                                                <ul class="text-light">
                                                    <li><strong>SDLC Transformation:</strong> Led AI-driven SDLC transformation across 3 concurrent banking application releases with zero P1 defects.</li>
                                                    <li><strong>Agentic Workflows:</strong> Orchestrated AI agents for automated requirement analysis, test generation, and intelligent defect triage, reducing unplanned rework by 40%.</li>
                                                    <li><strong>Team Leadership:</strong> Managed a team of 5 engineers, mentoring them on AI governance, guardrails, and prompt engineering.</li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Experience Card 2-->
                            <div class="card shadow border-0 rounded-4 mb-5">
                                <div class="card-body p-5">
                                    <div class="row align-items-center gx-5">
                                        <div class="col text-center text-lg-start mb-4 mb-lg-0">
                                            <div class="bg-transparent p-4 rounded-4">
                                                <div class="text-primary fw-bolder mb-2">Jan 2024 - April 2025</div>
                                                <div class="small fw-bolder">Senior QA Engineer / AI Automation Lead</div>
                                                <div class="small text-light">iSON Xperiences</div>
                                                <div class="small text-light">Chennai, India</div>
                                            </div>
                                        </div>
                                        <div class="col-lg-8">
                                            <div>
                                                <ul class="text-light">
                                                    <li>Spearheaded AI automation testing initiatives within the core banking domain, collaborating with development teams to resolve critical defects.</li>
                                                    <li>Integrated AI-driven test capabilities leveraging Healenium for self-healing locators and LangChain/CrewAI for test data generation.</li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Experience Card 3-->
                            <div class="card shadow border-0 rounded-4 mb-5">
                                <div class="card-body p-5">
                                    <div class="row align-items-center gx-5">
                                        <div class="col text-center text-lg-start mb-4 mb-lg-0">
                                            <div class="bg-transparent p-4 rounded-4">
                                                <div class="text-primary fw-bolder mb-2">Sept 2018 - Jan 2024</div>
                                                <div class="small fw-bolder">Software Test Engineer</div>
                                                <div class="small text-light">Techies Infotech Pvt Ltd</div>
                                                <div class="small text-light">Chennai, India</div>
                                            </div>
                                        </div>
                                        <div class="col-lg-8">
                                            <div>
                                                <ul class="text-light">
                                                    <li><strong>Framework Architecture:</strong> Built the company's first scalable automation framework from zero, standardizing it across 6 client projects.</li>
                                                    <li><strong>API & Mobile Testing:</strong> Designed REST API frameworks and delivered Android automation, reducing manual execution time from 3 days to 45 minutes.</li>
                                                    <li><strong>RPA:</strong> Deployed UiPath bots for data validation, saving 12 person-hours per sprint cycle.</li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <!-- Education Section-->
                        <section>
                            <h2 class="text-secondary fw-bolder mb-4">Education</h2>
                            <div class="card shadow border-0 rounded-4 mb-5">
                                <div class="card-body p-5">
                                    <div class="row align-items-center gx-5">
                                        <div class="col text-center text-lg-start mb-4 mb-lg-0">
                                            <div class="bg-transparent p-4 rounded-4">
                                                <div class="text-secondary fw-bolder mb-2">Aug 2012 - June 2016</div>
                                                <div class="mb-2">
                                                    <div class="small fw-bolder">Kongu Engineering College</div>
                                                    <div class="small text-light">Perundurai, Erode</div>
                                                </div>
                                                <div class="fst-italic">
                                                    <div class="small text-light">Bachelor's in</div>
                                                    <div class="small text-light">Civil Engineering</div>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-lg-8"><div class="text-light">Graduated with foundational engineering principles. <br><br> <strong>Languages:</strong> English, Tamil, Romanian (Elementary)</div></div>
                                    </div>
                                </div>
                            </div>
                        </section>

                        <!-- Divider-->
                        <div class="pb-5"></div>

                        <!-- Skills Section-->
                        <section>
                            <div class="card shadow border-0 rounded-4 mb-5">
                                <div class="card-body p-5">
                                    <div class="mb-5">
                                        <div class="d-flex align-items-center mb-4">
                                            <div class="feature bg-primary bg-gradient-primary-to-secondary text-white rounded-3 me-3"><i class="bi bi-tools"></i></div>
                                            <h3 class="fw-bolder mb-0"><span class="text-gradient d-inline">Core Competencies</span></h3>
                                        </div>
                                        <div class="row row-cols-1 row-cols-md-2 mb-4">
                                            <div class="col mb-4 mb-md-0"><div class="d-flex align-items-center bg-transparent rounded-4 p-3 h-100 border border-secondary border-opacity-25 text-light">Semantic Kernel & LangChain</div></div>
                                            <div class="col"><div class="d-flex align-items-center bg-transparent rounded-4 p-3 h-100 border border-secondary border-opacity-25 text-light">CrewAI & AutoGen</div></div>
                                        </div>
                                        <div class="row row-cols-1 row-cols-md-2 mb-4">
                                            <div class="col mb-4 mb-md-0"><div class="d-flex align-items-center bg-transparent rounded-4 p-3 h-100 border border-secondary border-opacity-25 text-light">GitHub Actions (CI/CD)</div></div>
                                            <div class="col"><div class="d-flex align-items-center bg-transparent rounded-4 p-3 h-100 border border-secondary border-opacity-25 text-light">Healenium & UiPath</div></div>
                                        </div>
                                    </div>
                                    
                                    <div class="mb-0">
                                        <div class="d-flex align-items-center mb-4">
                                            <div class="feature bg-primary bg-gradient-primary-to-secondary text-white rounded-3 me-3"><i class="bi bi-code-slash"></i></div>
                                            <h3 class="fw-bolder mb-0"><span class="text-gradient d-inline">Architecture & Languages</span></h3>
                                        </div>
                                        <div class="row row-cols-1 row-cols-md-3 mb-4">
                                            <div class="col mb-4 mb-md-0"><div class="d-flex align-items-center bg-transparent rounded-4 p-3 h-100 border border-secondary border-opacity-25 text-light">C# / .NET Core</div></div>
                                            <div class="col mb-4 mb-md-0"><div class="d-flex align-items-center bg-transparent rounded-4 p-3 h-100 border border-secondary border-opacity-25 text-light">Java</div></div>
                                            <div class="col"><div class="d-flex align-items-center bg-transparent rounded-4 p-3 h-100 border border-secondary border-opacity-25 text-light">REST API</div></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </section>
"""

    # We need to replace everything from <!-- Experience Section--> to the end of the col-lg-7 div.
    # The container in resume.html is: <div class="col-lg-7"> ... all these sections ... </div>
    pattern = r'<!-- Experience Section-->.*?</section>\s*</div>'
    html = re.sub(pattern, new_content + '\n</div>', html, flags=re.DOTALL)
    
    with open('resume.html', 'w', encoding='utf-8') as f:
        f.write(html)


def update_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    old_desc = "Crafting modern QA automation frameworks with clean code, robust testing strategies, and scalable digital architecture."
    new_desc = "AI Orchestrator & Lead Quality Engineer building intelligent, scalable automation frameworks and agentic workflows."
    html = html.replace(old_desc, new_desc)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

update_resume()
update_index()
