```csharp
namespace Project.Infrastructure.Persistence.Multitenant.Configurations.Brands
{
    public class BrandConfiguration : IEntityTypeConfiguration<Brand>
    {
        public void Configure(EntityTypeBuilder<Brand> builder)
        {
            builder.ToTable("Brands");

            builder.HasKey(brand => brand.Id);

            builder.Property(brand => brand.Id)
                .IsRequired();

            builder.Property(brand => brand.Name)
                .IsRequired();

            builder.Property(brand => brand.Title);

            builder.Property(brand => brand.CreatedAt)
                .IsRequired();

            builder.Property(brand => brand.UpdatedAt)
                .IsRequired();

            builder.HasOne(brand => brand.Organization)
                .WithMany(organization => organization.Brands)
                .HasForeignKey(brand => brand.OrganizationId)
                .OnDelete(DeleteBehavior.Cascade)
                .IsRequired();

            builder.HasOne(brand => brand.Category)
                .WithMany()
                .HasForeignKey(brand => brand.CategoryId)
                .OnDelete(DeleteBehavior.Cascade)
                .IsRequired();

            builder.HasMany(brand => brand.Users)
                .WithMany(user => user.Brands)
                .UsingEntity<BrandUser>();
        }
    }
}
```