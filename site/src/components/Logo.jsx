function Logo () {
    return(
        <div className="Logo">                                    
            <svg width="37.2" height="40" viewBox="0 0 372 400" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g filter="url(#filter0_d_32_6)">
            <path d="M297.164 248.196C303.829 244.514 312 249.335 312 256.949V330C312 335.523 307.523 340 302 340H169.778C159.448 340 155.9 326.243 164.942 321.247L297.164 248.196Z" fill="#FF7F50"/>
            <path d="M40 156.949C40.0002 149.335 48.1711 144.514 54.8359 148.196L205.157 231.247C212.043 235.051 212.043 244.949 205.157 248.753L54.8359 331.804C48.1712 335.486 40.0003 330.665 40 323.051V156.949Z" fill="#FF7F50"/>
            <path d="M296.164 48.1963C302.829 44.5142 311 49.335 311 56.9492V223.051C311 230.665 302.829 235.486 296.164 231.804L145.843 148.753C138.957 144.949 138.957 135.051 145.843 131.247L296.164 48.1963Z" fill="#FF7F50"/>
            <path d="M182.222 40C192.552 40.0004 196.1 53.7568 187.058 58.7529L54.8359 131.804C48.1712 135.486 40.0003 130.665 40 123.051V50C40 44.4772 44.4772 40 50 40H182.222Z" fill="#FF7F50"/>
            </g>
            <g filter="url(#filter1_i_32_6)">
            <rect x="20" y="20" width="312" height="340" rx="20" fill="white" fill-opacity="0.1"/>
            </g>
            <defs>
            <filter id="filter0_d_32_6" x="0" y="0" width="372" height="400" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
            <feFlood flood-opacity="0" result="BackgroundImageFix"/>
            <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
            <feOffset dx="10" dy="10"/>
            <feGaussianBlur stdDeviation="25"/>
            <feComposite in2="hardAlpha" operator="out"/>
            <feColorMatrix type="matrix" values="0 0 0 0 1 0 0 0 0 0.498039 0 0 0 0 0.313726 0 0 0 0.9 0"/>
            <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_32_6"/>
            <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_32_6" result="shape"/>
            </filter>
            <filter id="filter1_i_32_6" x="20" y="20" width="312" height="340" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
            <feFlood flood-opacity="0" result="BackgroundImageFix"/>
            <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
            <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
            <feOffset/>
            <feGaussianBlur stdDeviation="5"/>
            <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
            <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0"/>
            <feBlend mode="normal" in2="shape" result="effect1_innerShadow_32_6"/>
            </filter>
            </defs>
            </svg>
            {' '}
            <span className="Logo_1">BIO</span>
            <span className="Logo_2">solution</span>
        </div>
    )
}
export default Logo;