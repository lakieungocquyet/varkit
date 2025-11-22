import {useState} from "react";

function HeaderNavigation () {
    const [openSection, setOpenSection] = useState(null);
    const toggleSection = (name) => {
        setOpenSection(prev => prev === name ? null : name);
    };
    return(
        <div className={`header_navigation`} >
            <div className={`dropdown_container`}>
                <button className="dropdown_button">
                    <span className="dropdown_button_label">
                        Home
                    </span>
                </button>
            </div>
            <div className={`dropdown_container ${openSection === "installation" ? "open" : ""}`}>
                <button className="dropdown_button" onClick={() => toggleSection("installation")}>
                    <span className="dropdown_button_label">
                        Installation
                    </span>
                </button>
            </div>
            <div className={`dropdown_container`}>
                <button className="dropdown_button">
                    <span className="dropdown_button_label">
                        Documentation
                    </span>
                </button>
            </div>
            <div className={`dropdown_container ${openSection === "about" ? "open" : ""}`}>
                <button className="dropdown_button" onClick={ () => toggleSection("about")}>
                    <span className="dropdown_button_label" >
                        About
                    </span>
                </button>
            </div>
            {(openSection === "installation" || openSection === "about")  && (
                <div className="dropdown_panel">
                    { openSection === "about" && (
                        <div className="about_panel">
                            <button>
                                About us
                            </button>
                            <button>
                                License
                            </button>
                        </div>
                        )

                    }
                </div>
                )
            }
        </div>
    )
}
export default HeaderNavigation;