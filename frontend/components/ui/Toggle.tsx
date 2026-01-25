import { InputHTMLAttributes, forwardRef } from 'react'
import { clsx } from 'clsx'

interface ToggleProps extends Omit<InputHTMLAttributes<HTMLInputElement>, 'type'> {
  label?: string
}

export const Toggle = forwardRef<HTMLInputElement, ToggleProps>(
  ({ className, label, checked, onChange, ...props }, ref) => {
    return (
      <label className="inline-flex items-center cursor-pointer">
        <div className="relative">
          <input
            ref={ref}
            type="checkbox"
            className="sr-only"
            checked={checked}
            onChange={onChange}
            {...props}
          />
          <div
            className={clsx(
              'w-10 h-6 rounded-full transition-colors duration-200',
              checked ? 'bg-primary-600' : 'bg-gray-300'
            )}
          />
          <div
            className={clsx(
              'absolute left-0.5 top-0.5 w-5 h-5 bg-white rounded-full',
              'transition-transform duration-200 shadow-sm',
              checked && 'transform translate-x-4'
            )}
          />
        </div>
        {label && (
          <span className="ml-3 text-sm font-medium text-gray-700">
            {label}
          </span>
        )}
      </label>
    )
  }
)

Toggle.displayName = 'Toggle'
