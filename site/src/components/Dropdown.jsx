import { useState, useRef, useEffect } from 'react';

function Dropdown({
	label,
	items = [],
	placeholder = 'Chọn...',
	disabled = false,
	className = '',
	icon = <svg xmlns="http://www.w3.org/2000/svg" height="22px" viewBox="0 -960 960 960" width="22px" fill="#FFFFFF"><path d="m291-453-51-51 240-240 240 240-51 51-189-189-189 189Z"/></svg>,
	onSelect, // optional: fires for any item selection
}) {

	const [isOpen, setIsOpen] = useState(false);

	const dropdownRef = useRef(null);
	const hoverTimeout = useRef(null);
	
	// helpers để lấy label/value của item
	const getItemLabel = (item) => {
		if (typeof item === 'object' && item !== null) {
			if (item.label != null) return String(item.label);
			if (item.value != null) return String(item.value);
		}
		return String(item ?? '');
	};
	const getItemValue = (item) => {
		if (typeof item === 'object' && item !== null) {
			if (item.value !== undefined) return item.value;
			return item;
		}
		return item;
	};

	useEffect(() => {
		return () => {
			if (hoverTimeout.current) 
				clearTimeout(hoverTimeout.current);
		};
	}, []);

	const handleMouseEnter = () => {
		if (disabled) 
			return;
		if (hoverTimeout.current) 
			clearTimeout(hoverTimeout.current);
		setIsOpen(true);
	};

	const handleMouseLeave = () => {
		if (hoverTimeout.current) 
			clearTimeout(hoverTimeout.current);
		hoverTimeout.current = setTimeout(() => setIsOpen(false), 150);
	};

	const handleItemClick = (item, index, e) => {
		if (hoverTimeout.current) 
			clearTimeout(hoverTimeout.current);

		const value = getItemValue(item);
		const labelText = getItemLabel(item);

		// Ưu tiên onClick của item nếu có
		if (item && typeof item === 'object' && typeof item.onClick === 'function') {
			item.onClick({ item, index, value, label: labelText, event: e });
		}

		// Gọi onSelect chung nếu được truyền vào
		if (typeof onSelect === 'function') {
			onSelect({ item, index, value, label: labelText, event: e });
		}

		setIsOpen(false);
	};

	return (
		<div 
			className={`dropdown-container ${className}`}
			ref={dropdownRef}
			onMouseEnter={handleMouseEnter}
			onMouseLeave={handleMouseLeave}
		>
			<button
				type="button"
				disabled={disabled}
				className={`dropdown-button ${isOpen ? 'dropdown-open' : ''}`} aria-expanded={isOpen} aria-haspopup="true"
			>
				<span className="dropdown_label">{placeholder}</span>
				<span className={`dropdown-icon ${isOpen ? 'dropdown-icon-rotated' : ''}`}>
					{icon}
				</span>
			</button>

			{isOpen && (
				<div className="dropdown-menu" role="menu">
					{items.length === 0 ? (<div className="dropdown-empty">No item found</div>) : 
						(
						items.map((item, index) => {
							const itemValue = getItemValue(item);
							const itemLabel = getItemLabel(item);
							const disabledItem = typeof item === 'object' && item.disabled;

							return (
								<button
									key={index}
									type="button"
									onClick={(e) => !disabledItem && handleItemClick(item, index, e)}
									className={`
										dropdown-item
										${disabledItem ? 'dropdown-item-disabled' : ''}
									`}
									disabled={disabledItem}
									role="menuitem"
								>
									{item?.icon && <span className="dropdown-item-icon">{item.icon}</span>}
									<span className="dropdown-item-text">{itemLabel}</span>
								</button>
							);
						})
					)}
				</div>
			)}
		</div>
	);
}

export default Dropdown;