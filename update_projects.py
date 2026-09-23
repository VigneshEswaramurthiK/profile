import re

def update_projects():
    with open('projects.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_content = """
                            <!-- Project Card 1-->
                            <div class="card overflow-hidden shadow rounded-4 border-0 mb-5">
                                <div class="card-body p-0">
                                    <div class="d-flex align-items-center">
                                        <div class="p-5">
                                            <h2 class="fw-bolder">AI-Driven SDLC Transformation</h2>
                                            <p>Led AI-driven SDLC transformation across 3 concurrent banking application releases. Owned the master strategy for integrating AI agents into the development lifecycle, ensuring all releases went live on schedule with zero P1 defects.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- Project Card 2-->
                            <div class="card overflow-hidden shadow rounded-4 border-0 mb-5">
                                <div class="card-body p-0">
                                    <div class="d-flex align-items-center">
                                        <div class="p-5">
                                            <h2 class="fw-bolder">Agentic QA Workflows</h2>
                                            <p>Orchestrated AI agents using Semantic Kernel and LangChain for automated requirement analysis, test generation, and intelligent defect triage. Established human-in-the-loop governance which reduced unplanned rework by 40%.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
							<!-- Project Card 3-->
                            <div class="card overflow-hidden shadow rounded-4 border-0">
                                <div class="card-body p-0">
                                    <div class="d-flex align-items-center">
                                        <div class="p-5">
                                            <h2 class="fw-bolder">Scalable Enterprise Framework</h2>
                                            <p>Built the company's first scalable automation framework from zero, which became the standard template across 6 subsequent client projects. Delivered robust mobile and API test coverage, cutting execution time from days to minutes.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
"""

    pattern = r'<!-- Project Card 1-->.*</div>\s*</div>\s*</div>\s*</section>'
    html = re.sub(pattern, new_content + '\n                        </div>\n                    </div>\n                </div>\n            </section>', html, flags=re.DOTALL)
    
    with open('projects.html', 'w', encoding='utf-8') as f:
        f.write(html)

update_projects()
