import * as React from "react";
import { cn } from "@/lib/utils";

interface GoldButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "solid" | "outline";
  size?: "md" | "lg";
}

export const GoldButton = React.forwardRef<HTMLButtonElement, GoldButtonProps>(
  ({ className, variant = "solid", size = "lg", children, ...props }, ref) => {
    const base =
      "group relative inline-flex items-center justify-center font-semibold tracking-wider uppercase transition-all duration-300 rounded-md overflow-hidden focus:outline-none focus:ring-2 focus:ring-gold focus:ring-offset-2 focus:ring-offset-background";
    const sizes = {
      md: "px-6 py-3 text-xs",
      lg: "px-8 py-5 text-sm",
    };
    const variants = {
      solid:
        "bg-gradient-gold text-ink shadow-gold hover:shadow-[0_25px_70px_-15px_oklch(0.78_0.13_80/0.6)] hover:-translate-y-0.5",
      outline:
        "border border-gold/50 text-gold hover:bg-gold/10 hover:border-gold",
    };
    return (
      <button
        ref={ref}
        className={cn(base, sizes[size], variants[variant], className)}
        {...props}
      >
        <span className="relative z-10 flex items-center gap-2">{children}</span>
        {variant === "solid" && (
          <span className="absolute inset-0 -translate-x-full group-hover:translate-x-full transition-transform duration-1000 bg-gradient-to-r from-transparent via-white/30 to-transparent" />
        )}
      </button>
    );
  }
);
GoldButton.displayName = "GoldButton";
